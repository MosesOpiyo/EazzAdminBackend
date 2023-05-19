import binascii
import os
from .email import send_welcome_email
from decouple import config
from rest_framework import serializers
from .models import Account,Profile

from Products.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','username']

    def save(self,request):
        if request.user:
            user = Account(email=self.validated_data['email'],username = self.validated_data['username'],employee_id=binascii.hexlify(os.urandom(8)).decode(),server_code=binascii.hexlify(os.urandom(10)).decode(),admin=request.user.employee_id,establishment=request.user.establishment,customers=0,sales=0)
            password = Account.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889@")
            user.set_password(password)
            user.save()
            send_welcome_email(name=user.username,password=password,receiver=user.email)
            employee = Employees.objects.create(employee=user.employee_id)
            employee.save()
            db = ProductDatabase.objects.prefetch_related('employees','products').get(id=request.user.establishment)
            db.employees.add(employee)
            db.save()
        
        return user
    
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
        fields = ['id','email','username','establishment','sales','till_number','customers','is_company_admin','employee_id']

class TillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['till_number']

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'