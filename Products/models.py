from django.db import models
from Authentication.models import Account
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

class Product(models.Model):
    item_number = models.IntegerField(null=True)
    item_name = models.CharField(max_length=500,null=True)
    item_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.item_name

class ProductDatabase(models.Model):
    establishment = models.CharField(max_length=100,null=True)
    admin = models.IntegerField(null=True)
    products = models.ManyToManyField(Product,null=True)