# Generated by Django 4.0 on 2023-04-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevenueRecords', '0007_rename_percentage_revenuerecord_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuerecord',
            name='week',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
