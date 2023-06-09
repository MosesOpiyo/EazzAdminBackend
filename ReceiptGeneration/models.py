from django.db import models
import binascii
import os
from datetime import datetime

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_number = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    

class Receipt(models.Model):

    id = models.AutoField(primary_key=True)
    published = models.DateTimeField(default = datetime.now)
    receipt_number = models.CharField(max_length=12,null=True)
    store_name = models.CharField(max_length=100,null=True)
    server = models.CharField(max_length=20,null=True)
    server_name = models.CharField(max_length=40,null=True)
    till_number = models.CharField(null=True,max_length=8)
    items = models.ManyToManyField(Item)
    sub_total = models.IntegerField(null=True)
    overseer = models.CharField(max_length=20,null=True)
    VAT = models.IntegerField(null=True)
    total = models.IntegerField(default=0)
    day = models.IntegerField(null=True)
    week = models.IntegerField(null=True)

    def __str__(self):
        return self.receipt_number 
    
    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_number()
        return super().save(*args, **kwargs)
    
    def getTotal(self):
        total = 0
        for price in range(0, len(Receipt.items)):
           total = total + self.items.price
 
    
    @classmethod
    def generate_number(cls):
        return binascii.hexlify(os.urandom(6)).decode()

