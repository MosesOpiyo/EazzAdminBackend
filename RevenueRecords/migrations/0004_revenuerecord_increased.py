# Generated by Django 4.0 on 2023-04-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevenueRecords', '0003_revenuerecord_week_alter_revenuerecord_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenuerecord',
            name='increased',
            field=models.BooleanField(default=False),
        ),
    ]
