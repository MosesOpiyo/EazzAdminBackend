from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *

@api_view(["POST"])
def databaseCreation(request):
    data = {}
    database = DatabaseSerializers(data=request.data)

    if database.is_valid(): 
        database.save()
        data = "New Database created"
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data = database.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def Products(request):
    data = {}
    product_serializer = ProductsSerializers(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
        return Response(data="Product added",status=status.HTTP_201_CREATED)
    else:
        product_serializer.errors
        return Response(data="Error",status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def getProductDatabases(request):
    data = {}
    db = ProductDatabase.objects.all() 
    data = GetProductDatabaseSerializers(db,many=True).data
    return Response(data,status=status.HTTP_200_OK)

