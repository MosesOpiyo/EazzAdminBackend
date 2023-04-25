from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product,ProductDatabase
from Products.serializers import GetProductsSerializers
from datetime import date

from RevenueRecords.views import RecordView
from .serializers import *
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProduct(request,id,number):
    db = ProductDatabase.objects.get(id=request.user.establishment)
    
    if db.employees.filter(employee=request.user.employee_id).exists:
        product = db.products.get(item_number=number)
        receipt = Receipt.objects.get(id=id)
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

    receipt = Receipt.objects.get(id=id)
    data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetEmployeeReceipts(request):
    data = {}

    receipt = Receipt.objects.filter(server=request.user.server_code,server_name=request.user.username)
    data = GetReceiptSerializers(receipt,many=True).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ReceiptView(request):
    data = {}

    my_date = date.today()
    year, week_num, day_of_week = my_date.isocalendar()
    receipt = Receipt.objects.create(
        server = request.user.server_code,
        server_name = request.user.username,
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
   
    receipt = Receipt.objects.get(id=id) 
    for item in receipt.items.all():
        total.append(item.price)
    receipt.total = sum(total)
    receipt.save()
    employee_receipts = Receipt.objects.filter(server=receipt.server)
    employee = Account.objects.get(server_code=receipt.server)
    for receipt in employee_receipts:
        total.append(receipt.total)
        new_total = sum(total) 
    employee.sales = new_total - receipt.total
    employee.customers = employee.customers + 1
    employee.save()
    data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_201_CREATED)
    

@api_view(["GET"])   
@permission_classes([IsAuthenticated])
def CheckReceipt(request):
    my_date = date.today()
    year, week_num, day_of_week = my_date.isocalendar()
    receipts = Receipt.objects.filter(server=request.user.server_code)
    for receipt in receipts:
        if receipt.week != week_num:
            receipts.delete()
        else:
            return True
   
    

