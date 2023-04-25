from django.db import models
from Authentication.models import Account

class RevenueRecord(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    week = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    percent = models.IntegerField(null=True)
    increased = models.BooleanField(default=False)

    def __str__(self):
        return str(self.week) 
   
 