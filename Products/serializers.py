from rest_framework import serializers
from django.db import models

from .models import Product,ProductDatabase
from Authentication.serializers import UserSerializer

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self):
        product = Product(item_number=self.validated_data['item_number'],item_name=self.validated_data['item_name'],item_price=self.validated_data['item_price'])
        product.save
        return product
    
class GetProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DatabaseSerializers(serializers.ModelSerializer):
    products = ProductsSerializers(read_only=True)
    class Meta:
        model = ProductDatabase
        fields = '__all__'

    def create(request,validated_data):
        products_data = validated_data.pop('products')
        database = ProductDatabase.objects.create(
            **validated_data
        )
        for product_data in products_data:
            products = Product.objects.create(
                item_number = product_data.get('item_number'),
                item_name = product_data.get('item_name'),
                item_price = product_data.get('item_price'),
            )
            
            database.products.add(products)
            database.admin.add(request.user)
            database.save()
        return database
