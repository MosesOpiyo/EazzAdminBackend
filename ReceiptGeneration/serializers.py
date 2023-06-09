from rest_framework import serializers
from Authentication.models import Account
from django.db import models

from .models import Item,Receipt
from Authentication.serializers import UserSerializer

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def save(self):
        items = Item(item_number=self.validated_data['item_number'],name=self.validated_data['name'],price=self.validated_data['price'])
        items.save
        return items
    
class GetItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_number','name','price']

class ReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = ['id','receipt_number','server','server_name','total','items']

    def create(request,validated_data):
        item_data = validated_data.pop('items')
        receipt = Receipt.objects.create(
            **validated_data
        )
        for item_data in item_data:
            items = Item.objects.create(
                name = item_data.get('name'),
                price = item_data.get('price'),
            )
            
            receipt.items.add(items)
            receipt.save()
        return receipt

class GetEmployeeSalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['total']          
            
class GetReceiptSerializers(serializers.ModelSerializer):
    items = GetItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = ['id','receipt_number','store_name','server','till_number','server_name','total','VAT','items']

class IncreaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['total']