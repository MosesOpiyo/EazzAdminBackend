from django.urls import path
import Employees.views as views

urlpatterns = [
    path("Employees",views.Employees,name="employees"),
    path("EmployeeSales",views.EmployeeSales,name="employee_sales")
]