# Generated by Django 4.0 on 2023-04-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevenueRecords', '0008_alter_revenuerecord_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuerecord',
            name='week',
            field=models.IntegerField(null=True),
        ),
    ]
