from django.urls import path
import ReceiptGeneration.views as views

urlpatterns = [
    path("Receipt",views.ReceiptView,name="record"),
    path("EmployeeSales/<int:id>",views.EmployeeSales,name="sales"),
    path("NewReceipt/<int:id>",views.NewReceipt,name="record"),
    path("EmployeeReceipts",views.GetEmployeeReceipts,name="employee_receipts"),
    path("LatestReceipt",views.GetEmployeeLatestReceipt,name="latest"),
    path("Latest",views.GetEmployeeLatest,name="employee_latest"),
    path("ReceiptItems/receipt=<int:id>/number=<int:number>",views.getProduct,name="product"),
    path("CheckReceipts",views.CheckReceipt,name="check"),
]