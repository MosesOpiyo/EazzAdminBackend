from django.urls import path
import Products.views as views

urlpatterns = [
    path("Products",views.databaseCreation,name="products")
   
]