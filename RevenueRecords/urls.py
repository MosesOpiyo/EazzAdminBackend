from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import RevenueRecords.views as views

urlpatterns = [
    path("Record/<int:id>",views.RecordView,name="record"),
    path("AllRecord/",views.get_all_record,name="record"),
    path("previous_record",views.get_record,name="previous_record"),
    path("Percentage_employee_display",views.increase_or_decrease_for_employee,name="percentage_employee_display"),
    path("Percentage",views.increase_or_decrease,name="percentage"),
]