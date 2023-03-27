from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product
from Products.serializers import GetProductsSerializers


from .serializers import *
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProduct(request,number):
    data = {}
    product = Product.objects.get(item_number = number)
    data = GetProductsSerializers(product).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ReceiptView(request):
    data = {}
    receipt_serializer = ReceiptSerializers(data=request.data)

    if receipt_serializer.is_valid(): 
        receipt_serializer.validated_data['server'] = request.user.id
        receipt_serializer.save()
        receipt = Receipt.objects.filter(server_name=request.user.username).order_by('-published')[0]
        data = GetReceiptSerializers(receipt).data
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data = receipt_serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(["DElETE"])   
@permission_classes([IsAuthenticated])
def NewReceipt():
    receipt = Receipt.objects.all()
    receipt.delete() 
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ReceiptItems(request,pk):
    data = {}
    total = []
    item_serializer = ItemsSerializers(data=request.data,many=True)
    receipt = Receipt.objects.get(pk=pk)
    if item_serializer.is_valid():
        item_serializer.save()
        items = Item.objects.all()
        receipt.items.set(items)
        for item in Item.objects.all():
            total.append(item.price)
            receipt.total = sum(total)
        receipt.save()
        data = GetReceiptSerializers(receipt).data
    return Response(data,status=status.HTTP_202_ACCEPTED)