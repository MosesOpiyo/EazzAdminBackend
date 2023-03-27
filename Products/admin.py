from django.contrib import admin
from .models import Product,ProductDatabase

# Register your models here.
admin.site.register(Product),
admin.site.register(ProductDatabase)