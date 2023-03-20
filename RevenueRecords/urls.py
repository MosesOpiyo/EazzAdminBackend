from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import RevenueRecords.views as views

urlpatterns = [
    path("Record",views.RecordView,name="record")
]