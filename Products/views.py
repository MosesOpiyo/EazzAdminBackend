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
    if request.user.is_authenticated:
        db = ProductDatabase.objects.get(id=request.user.establishment)
        if db.employees.filter(employee=request.user.employee_id).exists:
            product_resource = ProductsResources()
            dataset = Dataset()
            new_products = request.FILES['my_file']
            imported_data = dataset.load(new_products.read(),format='xlsx')
            for data in imported_data:
                values = Product.objects.create(
                   item_number = data[0],
                   item_name = data[1],
                   item_price = data[2]
                )
                values.save()
                db.products.add(values)
            data=GetProductDatabaseSerializers(db).data
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            data="UNAUTHORIZED"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED) 
    else:
        data="UNAUTHORIZED"
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addProducts(request):
    data = {}
    product_serializers = ProductsSerializers(data=request.data)
    db = ProductDatabase.objects.get(id=request.user.establishment)
    
    if product_serializers.is_valid():
        if db.employees.filter(employee=request.user.employee_id).exists:
          product = product_serializers.save()
          
          data = "Product added"
          return Response(data,status=status.HTTP_201_CREATED)
        else:
            data = "Unauthorized"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)
    else:
        data = product_serializers.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


        
        
        

