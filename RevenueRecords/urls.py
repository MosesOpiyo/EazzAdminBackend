from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import RevenueRecords.views as views

urlpatterns = [
    path("Record",views.RecordView,name="record"),
    path("previous_record",views.get_record,name="previous_record"),
    path("Percentage",views.increase_or_decrease,name="percentage"),
]