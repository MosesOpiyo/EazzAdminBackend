from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import pytz
from datetime import date

from ReceiptGeneration.models import Receipt
from .serializers import *
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def RecordView(request,id):
    data = {}

    my_date = date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    receipt = Receipt.objects.select_related('items').get(id=id)
    admin = Account.objects.get(employee_id=request.user.admin)
    records = RevenueRecord.objects.select_related('account').all()
    for record in records:
        if record.account == admin and record.week == week_num:
            record.amount = record.amount + receipt.total
            record.increase = 0
            increase = (receipt.total / record.amount)
            record.increase = increase * 100
            record.save()
            data =  GetRecordSerializer(record).data
            return Response(data,status=status.HTTP_200_OK) 
        
    new_record = RevenueRecord.objects.create(account=admin,week=week_num,amount=0)
    entry_receipt = Receipt.objects.prefetch_related('items').get(id=id)
    new_record.amount = 0 + entry_receipt.total
    new_record.save()
    data = GetRecordSerializer(new_record).data
    return Response(data,status=status.HTTP_201_CREATED) 
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_record(request):
    
    admin = Account.objects.get(id=request.user.id)
    record = RevenueRecord.objects.select_related('account').filter(account=admin)
    data =  GetRecordSerializer(record,many=True).data
    return Response(data,status = status.HTTP_200_OK)
            
            
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_record(request):
    data = {}
    my_date = date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    admin = Account.objects.get(id=request.user.id)
    record = RevenueRecord.objects.select_related('account').get(account=admin, week=week_num - 1)
    data =  GetRecordSerializer(record).data
    return Response(data,status = status.HTTP_200_OK)
     
@api_view(["GET"])
def increase_or_decrease(request):
    my_date = date.today()  
    year, week_num, day_of_week = my_date.isocalendar()

    data = {}
    admin = Account.objects.get(id=request.user.id)
    prev_record = RevenueRecord.objects.select_related('account').get(account=admin, week=week_num - 1)
    prev_record.percent = None
    prev_record.save
    current_record = RevenueRecord.objects.select_related('account').get(account=admin, week=week_num)
    if current_record.amount > prev_record.amount:
        increase = current_record.amount - prev_record.amount
        percentage_increase = (increase / prev_record.amount)
        prev_record.increased = False
        prev_record.percent = percentage_increase * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        decrease = prev_record.amount - current_record.amount
        percentage_decrease = (decrease / prev_record.amount)
        prev_record.increased = True
        prev_record.percent = percentage_decrease * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)
    
    
@api_view(["GET"])
def increase_or_decrease_for_employee(request):
    my_date = date.today()  
    year, week_num, day_of_week = my_date.isocalendar()

    data = {}
    admin = Account.objects.get(employee_id=request.user.admin)
    prev_record = RevenueRecord.objects.select_related('account').get(account=admin, week=week_num - 1)
    prev_record.percent = None
    prev_record.save
    current_record = RevenueRecord.objects.select_related('account').get(account=admin, week=week_num)
    if current_record.amount > prev_record.amount:
        increase = current_record.amount - prev_record.amount
        percentage_increase = (increase / prev_record.amount)
        prev_record.increased = False
        prev_record.percent = percentage_increase * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        decrease = prev_record.amount - current_record.amount
        percentage_decrease = (decrease / prev_record.amount)
        prev_record.increased = True
        prev_record.percent = percentage_decrease * 100
        prev_record.save()
        data = GetRecordSerializer(prev_record).data
        return Response(data,status=status.HTTP_200_OK)
    


    

