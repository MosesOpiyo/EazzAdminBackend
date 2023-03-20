from django.db import models
from Authentication.models import Account

class RevenueRecord(models.Model):
    account = models.OneToOneField(Account,on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return self.account.username
   
