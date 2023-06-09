from django.urls import path
import Products.views as views

urlpatterns = [
    path("Products",views.databaseCreation,name="products"),
    path("GetProducts",views.getProductDatabases,name="get"),
    path("ImportData",views.importExcel,name="import_data"),
    path("AddProduct",views.addProducts,name="new_product"),
    path("Count",views.getProductCount,name="count")
   
]