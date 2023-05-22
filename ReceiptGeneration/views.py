from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product,ProductDatabase
from Products.serializers import GetProductsSerializers
from datetime import date


from RevenueRecords.models import RevenueRecord
from .serializers import *
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProduct(request,id,number):
    db = ProductDatabase.objects.prefetch_related('employees','products').get(id=request.user.establishment)
    
    if db.employees.prefetch_related('employees','products').filter(employee=request.user.employee_id).exists:
        product = db.products.get(item_number=number)
        receipt = Receipt.objects.prefetch_related('items').get(id=id)
        item = Item.objects.create(
            item_number = product.item_number,
            name = product.item_name,
            price = product.item_price
        )

        receipt.items.add(item)
        receipt_items = receipt.items
        data = GetItemsSerializers(receipt_items,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        data = "Access to database denied"
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetReceipt(request,id):
    data = {}

    receipt = Receipt.objects.prefetch_related('items').get(id=id)
    data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetEmployeeReceipts(request):
    data = {}
    receipt = Receipt.objects.prefetch_related('items').filter(server=request.user.server_code,server_name=request.user.username).only('id','receipt_number','server','server_name','total','items')
    if receipt:
        data = GetReceiptSerializers(receipt,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        data = "No receipts Found"
        return Response(data,status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetEmployeeLatest(request):
    data = {}

    receipt = Receipt.objects.prefetch_related('items').filter(overseer=request.user.employee_id).latest('id')
    data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetEmployeeLatestReceipt(request):
    data = {}
    try:
        receipt = Receipt.objects.prefetch_related('items').filter(server=request.user.server_code).latest('id')
        data = GetReceiptSerializers(receipt).data
        return Response(data,status=status.HTTP_200_OK)
    except:
        data = "No receipts found"
        return Response(data,status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ReceiptView(request):
    data = {}

    my_date = date.today()
    store = ProductDatabase.objects.prefetch_related('employees','products').get(id=request.user.establishment)
    year, week_num, day_of_week = my_date.isocalendar()
    receipt = Receipt.objects.create(
        server = request.user.server_code,
        server_name = request.user.username,
        till_number = request.user.till_number,
        store_name = store.establishment,
        overseer = request.user.admin,
        day = day_of_week,
        week = week_num
    )
    data = receipt.id
    return Response(data,status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def NewReceipt(request,id):
    total = []
    data = {}
    my_date = date.today()
    year, week_num, day_of_week = my_date.isocalendar()
   
    receipt = Receipt.objects.prefetch_related('items').get(id=id) 
    for item in receipt.items.all():
        total.append(item.price)
    receipt.total = sum(total)
    receipt.sub_total = receipt.total * 0.16
    receipt.VAT = receipt.total - receipt.sub_total
    receipt.save()
    data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def EmployeeSales(request,id):
    employee = Account.objects.get(id=request.user.id)
    receipt = Receipt.objects.prefetch_related('items').get(id=id)
    employee.customers = employee.customers + 1
    prev_sales = employee.sales
    new_sales = prev_sales + receipt.total
    employee.sales = new_sales
    employee.save()
    return Response(data="Accepted",status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])   
@permission_classes([IsAuthenticated])
def CheckReceipt(request):
    my_date = date.today()
    year, week_num, day_of_week = my_date.isocalendar()
    receipts = Receipt.objects.prefetch_related('items').filter(server=request.user.server_code)
    for receipt in receipts:
        if receipt.week != week_num:
            account = Account.objects.get(id=request.user.id)
            account.sales = 0
            account.customers = 0
            receipts.delete()
        else:
            return True
   
    

