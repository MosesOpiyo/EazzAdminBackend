from django.contrib import admin
from .models import Product,ProductDatabase,Employees

# Register your models here.
admin.site.register(Product),
admin.site.register(ProductDatabase),
admin.site.register(Employees)