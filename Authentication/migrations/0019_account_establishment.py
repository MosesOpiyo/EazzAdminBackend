# Generated by Django 4.0 on 2023-04-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0018_alter_account_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='establishment',
            field=models.CharField(max_length=10, null=True),
        ),
    ]