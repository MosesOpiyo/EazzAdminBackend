# Generated by Django 4.0 on 2023-04-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_rename_profiles_productdatabase_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employee',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
