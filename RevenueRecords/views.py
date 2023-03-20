from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


from .serializers import *
from .models import *

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def RecordView(request):
    
    record_serializer = RecordSerializer(data=request.data)
    data = {}

    if record_serializer.is_valid():
        record = RevenueRecord.objects.get(account=request.user)
        print(record)
        if record:
           new_amount = record.amount + record_serializer.data['amount']
           record.amount = new_amount
           record.save()
           data = f"{record_serializer.data['amount']} added to your record."
           return Response(data,status = status.HTTP_202_ACCEPTED)
        elif not record:
           record_serializer.account = request.user
           record_serializer.save()
           data = f"New record created of {record.amount}"
           return Response(data,status = status.HTTP_201_CREATED)
    else:
        data = record_serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_record(request):
    data = {}
    record = RevenueRecord.objects.get(user=request.user)
    data =  GetRecordSerializer(record).data
    return Response(data,status = status.HTTP_200_OK)
     
@api_view(["GET"])
def get_employee_record(request):
    data = {}
    accounts = Account.objects.get(company = request.user.company)
    record = RevenueRecord.objects.filter(user=accounts)
    data =  GetRecordSerializer(record,many=True).data
    return Response(data,status = status.HTTP_200_OK)
     
    
