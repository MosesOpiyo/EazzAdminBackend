from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *

@api_view(['POST'])
def registration_view(request):
    
    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = f"Successfully created a new user under {account.username} with email {account.email}"
        return Response(data,status = status.HTTP_201_CREATED)
    else:
        data = serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):

    data = {}
    profile = Profile.objects.get(user=request.user)
    data =  ProfileSerializer(profile).data
    return Response(data,status = status.HTTP_200_OK)
