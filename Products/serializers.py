from rest_framework import serializers
from django.db import models

from .models import Product,ProductDatabase,Employees


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id','employee']
    
    def save(self):
        employee = Employees(employee=self.validated_data['employee'])
        employee.save()
        return employee

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self):
        product = Product.objects.create(item_number=self.validated_data['item_number'],item_name=self.validated_data['item_name'],item_price=self.validated_data['item_price'])
        product.save
        return product
    
class GetProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DatabaseSerializers(serializers.ModelSerializer):
    employees = EmployeeSerializers(many=True)
    products = ProductsSerializers(many=True)
    class Meta:
        model = ProductDatabase
        fields = '__all__'

    def create(request,validated_data):
        employees_data = validated_data.pop('employees')
        products_data = validated_data.pop('products')
        database = ProductDatabase.objects.create(
            **validated_data
        )
        
        for employee_data in employees_data:
            employees = Employees.objects.create(
                employee = employee_data.get('employee')
            ),

            database.employees.set(employees)
            database.save()
        for product_data in products_data:
            products = Product.objects.create(
                item_number = product_data.get('item_number'),
                item_name = product_data.get('item_name'),
                item_price = product_data.get('item_price'),
            )
            database.products.add(products)
            database.save()
        return database

class GetProductDatabaseSerializers(serializers.ModelSerializer):
    employees = EmployeeSerializers(many=True)
    products = ProductsSerializers(many=True)
    class Meta:
        model = ProductDatabase
        fields = '__all__'