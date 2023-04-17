from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from Authentication.models import Account
from Authentication.serializers import UserSerializer
from ReceiptGeneration.models import Receipt
from .serializers import EmployeeSalesSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Employees(request):
    data = {}
    if request.user.is_authenticated:
       employees = Account.objects.filter(admin=request.user.employee_id)
       data = UserSerializer(employees,many=True).data
       return Response(data,status=status.HTTP_200_OK)
    else:
       data = "Access Unauthorized"
       return Response(data,status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def EmployeeSales(request):
   data = {}
   if request.user.is_authenticated:
       employees = Account.objects.filter(admin=request.user.employee_id).order_by('-sales')
       data = EmployeeSalesSerializer(employees,many=True).data
       return Response(data,status=status.HTTP_200_OK)
   else:
       data = "Access Unauthorized"
       return Response(data,status=status.HTTP_401_UNAUTHORIZED)



      
      
        



