from django.contrib import admin
from .models import Product,ProductDatabase,Employees,Alert

# Register your models here.
admin.site.register(Product),
admin.site.register(ProductDatabase),
admin.site.register(Employees),
admin.site.register(Alert)