from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime

from ReceiptGeneration.models import Receipt
from .serializers import *
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def RecordView(request,id):
    data = {}

    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    receipt = Receipt.objects.get(id=id)
    admin = Account.objects.get(employee_id=request.user.admin)
    records = RevenueRecord.objects.all()
    for record in records:
        if record.account == admin and record.week == week_num:
            print("Receipt Amount:", receipt.total)
            record.save()
            overall_increase(increase=receipt.total, request=request)
            data = f"Amount {receipt.total} added"
            return Response(data,status=status.HTTP_200_OK) 
        
    new_record = RevenueRecord.objects.create(account=admin,week=week_num,amount=0)
    entry_receipt = Receipt.objects.get(id=id)
    new_record.amount = 0 + entry_receipt.total
    new_record.save()
    data = GetRecordSerializer(new_record).data
    return Response(data,status=status.HTTP_201_CREATED) 
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_record(request):
    
    admin = Account.objects.get(id=request.user.id)
    record = RevenueRecord.objects.filter(account=admin)
    data =  GetRecordSerializer(record,many=True).data
    return Response(data,status = status.HTTP_200_OK)
            
            
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
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()

    data = {}
    admin = Account.objects.get(employee_id=request.user.admin)
    prev_record = RevenueRecord.objects.get(account=admin, week=week_num - 1)
    prev_record.percent = None
    prev_record.save
    current_record = RevenueRecord.objects.get(account=admin, week=week_num)
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
    

@permission_classes([IsAuthenticated])
def overall_increase(increase,request):
    data = {}
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    admin = Account.objects.get(employee_id=request.user.admin)
    record = RevenueRecord.objects.get(account=admin, week=week_num)
    if record:
        record.save()
        data = GetRecordSerializer(record).data
        return Response(data,status=status.HTTP_202_ACCEPTED)
    else:
        data = "Record doesn't exist"
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    

