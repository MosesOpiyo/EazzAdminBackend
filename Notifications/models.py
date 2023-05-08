from django.db import models
from Authentication.models import Account 

class Notification(models.Model):
    customer = models.TextField(null=True)
    amount = models.IntegerField()
    server_code = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.server_code
