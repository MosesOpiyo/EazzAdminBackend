from django.urls import path
import ReceiptGeneration.views as views

urlpatterns = [
    path("Receipt",views.ReceiptView,name="record"),
    path("NewReceipt/<int:id>",views.NewReceipt,name="record"),
    path("EmployeeReceipts",views.GetEmployeeReceipts,name="employee_receipts"),
    path("ReceiptItems/receipt=<int:id>/number=<int:number>",views.getProduct,name="product"),
    path("CheckReceipts",views.CheckReceipt,name="check"),
]