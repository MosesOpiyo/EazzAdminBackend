from rest_framework import serializers
from django.db import models

from .models import Notification
    
class GetNotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'     