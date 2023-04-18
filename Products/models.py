from django.db import models

class Product(models.Model):
    item_number = models.IntegerField(null=True)
    item_name = models.TextField(null=True)
    item_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.item_name
    
class Employees(models.Model):
    employee = models.CharField(max_length=16,null=True,unique=True)
    
    def __str__(self):
        return self.employee

class ProductDatabase(models.Model):
    establishment = models.CharField(max_length=100,null=True)
    employees = models.ManyToManyField(Employees)
    products = models.ManyToManyField(Product,null=True)

    def __str__(self):
        return self.establishment