from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count


from .serializers import *
from .models import *

@api_view(["POST"])
def ReceiptView(request):
    data = {}
    receipt_serializer = ReceiptSerializers(data=request.data)

    if receipt_serializer.is_valid(): 
        receipt_serializer.save()
        receipt = Receipt.objects.filter(server_name=request.user.username).order_by('-published')[0]
        data = GetReceiptSerializers(receipt).data
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data = receipt_serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
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