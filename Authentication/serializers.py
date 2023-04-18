import binascii
import os
from rest_framework import serializers
from .models import Account,Profile

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','password','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self,request):
        if request.user:
            account = Account(email=self.validated_data['email'],username = self.validated_data['username'],employee_id=binascii.hexlify(os.urandom(8)).decode(),server_code=binascii.hexlify(os.urandom(10)).decode(),admin=request.user.employee_id)
        else:
            account = Account(email=self.validated_data['email'],username = self.validated_data['username'],employee_id=binascii.hexlify(os.urandom(8)).decode(),server_code=binascii.hexlify(os.urandom(10)).decode())
        account.set_password(self.validated_data['password'])
        print(f"New user,{account.username} has been created with email {account.email}")
        account.save()
        return account
    
class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','password','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        account = Account(email=self.validated_data['email'],username = self.validated_data['username'],employee_id=binascii.hexlify(os.urandom(8)).decode(),server_code=binascii.hexlify(os.urandom(10)).decode(),is_company_admin=True,code=binascii.hexlify(os.urandom(10)).decode())
        account.set_password(self.validated_data['password'])
        print(f"New user,{account.username} has been created with email {account.email}")
        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','username','establishment','sales','customers','is_company_admin','confirm_start_shift','confirm_end_shift','employee_id','date_joined','last_login']


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'