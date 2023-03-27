from django.urls import path
import ReceiptGeneration.views as views

urlpatterns = [
    path("Products",views.ReceiptView,name="products"),
    path("Products/number=<int:item_number>",views.ReceiptItems,name="item")
]