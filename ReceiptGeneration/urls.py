from django.urls import path
import ReceiptGeneration.views as views

urlpatterns = [
    path("Receipt",views.ReceiptView,name="record"),
    path("ReceiptItems/<int:pk>",views.ReceiptItems,name="items"),
    path("ReceiptItems/receipt=<int:id>/number=<int:number>",views.getProduct,name="product")
]