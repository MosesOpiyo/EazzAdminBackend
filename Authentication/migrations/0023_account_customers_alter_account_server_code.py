# Generated by Django 4.0 on 2023-04-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0022_account_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='customers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='server_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
