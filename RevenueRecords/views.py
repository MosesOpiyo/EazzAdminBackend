from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime


from .serializers import *
from .models import *

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def RecordView(request):
    data = {}

    record_serializer = RecordSerializer(data=request.data)
    if record_serializer.is_valid():
        if request.user.is_authenticated:
            my_date = datetime.date.today() 
            year, week_num, day_of_week = my_date.isocalendar()
            admin = Account.objects.get(employee_id=request.user.admin)
            obj,record = RevenueRecord.objects.get_or_create(account=admin, week=week_num)
            if not obj.week:
                obj.week = week_num
                obj.amount = record_serializer.data['amount']
                obj.save()
                data = GetRecordSerializer(obj).data
                return Response(data,status=status.HTTP_201_CREATED) 
                
            else:
                recent = obj.amount
                obj.amount = sum([recent,record_serializer.data['amount']])
                obj.save()
                data = GetRecordSerializer(obj).data
                return Response(data,status=status.HTTP_200_OK) 
            

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_record(request):
    data = {}
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    admin = Account.objects.get(id=request.user.id)
    record = RevenueRecord.objects.get(account=admin, week=week_num - 1)
    data =  GetRecordSerializer(record).data
    return Response(data,status = status.HTTP_200_OK)
     
@api_view(["GET"])
def increase_or_decrease(request):
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()

    data = {}
    admin = Account.objects.get(id=request.user.id)
    prev_record = RevenueRecord.objects.get(account=admin, week=week_num - 1)
    prev_record.percent = None
    prev_record.save
    current_record = RevenueRecord.objects.get(account=admin, week=week_num)
    if current_record.amount > prev_record.amount:
        increase = current_record.amount - prev_record.amount
        percentage_increase = (increase / current_record.amount)
        prev_record.increased = False
        prev_record.percent = percentage_increase * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)
    elif prev_record > current_record:
        decrease = prev_record.amount - current_record.amount
        percentage_decrease = (decrease / prev_record.amount)
        prev_record.increased = True
        prev_record.percent = percentage_decrease * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)

