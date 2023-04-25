from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from tablib import Dataset
from .resources import ProductsResources
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
        product = product_serializer.save()
        print(GetProductsSerializers(product).data)
        return Response(data="Product added",status=status.HTTP_201_CREATED)
    else:
        product_serializer.errors
        return Response(data="Error",status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def getProductDatabases(request):
    data = {}
    db = ProductDatabase.objects.get(id=request.user.establishment)
    if db.employees.filter(employee=request.user.employee_id).exists and request.user.is_authenticated:
        data = GetProductsSerializers(db.products,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        data = "Access unauthorized"
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def importExcel(request):
    data = {}
    product_serializer = ProductsSerializers(data=request.data,many=True)

    if product_serializer.is_valid():
        product = product_serializer.save()
        return Response(data="Product added",status=status.HTTP_201_CREATED)
    else:
        product_serializer.errors
        return Response(data="Error",status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addProducts(request):
    data = {}
    product_serializers = ProductsSerializers(data=request.data)
    db = ProductDatabase.objects.get(id=request.user.establishment)
    
    if product_serializers.is_valid():
        product_serializers.save()
        if db.employees.filter(employee=request.user.employee_id).exists:
          new_product = Product.objects.get(item_number = product_serializers.data['item_number'])
          db.products.add(new_product)
          db.save()
          data = "Product added"
          return Response(data,status=status.HTTP_201_CREATED)
        else:
            data = "Unauthorized"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)
    else:
        data = product_serializers.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


        
        
        

