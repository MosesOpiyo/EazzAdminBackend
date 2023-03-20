from rest_framework import serializers
from .models import RevenueRecord
from Authentication.serializers import UserSerializer

class RecordSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)
    class Meta:
        model = RevenueRecord
        fields = '__all__'
        

    def save(self):
        record = RevenueRecord(amount = self.validated_data['amount'],account = self.account)
        print(f"New record,{record.account.username}, amount {record.amount}")
        record.save()
        return record
    
class GetRecordSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)
    class Meta:
        fieds = '__all__'