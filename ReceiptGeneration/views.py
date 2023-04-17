from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product,ProductDatabase
from Products.serializers import GetProductsSerializers


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
def ReceiptView(request):
    data = {}

    receipt = Receipt.objects.create(
        server = request.user.id,
        server_name = request.user.username 
    )
    data = receipt.id
    return Response(data,status=status.HTTP_201_CREATED)
    
@api_view(["DElETE"])   
@permission_classes([IsAuthenticated])
def ProducedReceipt():
    receipt = Receipt.objects.all()
    receipt.delete() 
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ReceiptItems(request,pk):
    data = {}
    total = []
    sales = request.user.sales
    item_serializer = ItemsSerializers(data=request.data,many=True)
    receipt = Receipt.objects.get(pk=pk)
    if item_serializer.is_valid():
        item_serializer.save()
        items = Item.objects.all()
        receipt.items.set(items)
        for item in Item.objects.all():
            total.append(item.price)
            receipt.total = sum(total)
            request.user.sales = sales + receipt.total
        receipt.save()
        data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_202_ACCEPTED)