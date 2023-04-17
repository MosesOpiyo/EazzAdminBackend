from django.db import models

# Create your models here.
class EmployeeSale(models.Model):
    employee = models.CharField(max_length=200,null=True)
    sales = models.IntegerField(null=True)

    def __str__(self):
        return self.employee