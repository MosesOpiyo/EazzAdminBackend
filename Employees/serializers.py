from rest_framework import serializers
from  Authentication.models import Account

class EmployeeSalesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['username','customers','sales']