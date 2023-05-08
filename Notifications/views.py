from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import GetNotificationSerializers
from .models import Notification
# Create your views here.
@api_view(["GET"])
def NotificationView(request,name,amount,code):
    data = {}
    notification = Notification.objects.create(
       name = name,
       amount = amount,
       server_code = code
    )
    data = "Payment Succesful"
    return Response(data,status=status.HTTP_202_ACCEPTED)
    
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    data = {}
    notification = Notification.objects.get(server_code=request.user.server_code)
    if notification:
        data = GetNotificationSerializers(notification).data
        return Response(data,status=status.HTTP_200_OK)
    else:
        data = "No notification."
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def deleteNotifications(request):
    data = {}
    notification = Notification.objects.filter(server_code=request.user.server_code)
    notification.delete
    data = "Notification deleted"
    return Response(data,status=status.HTTP_200_OK)
    
    
