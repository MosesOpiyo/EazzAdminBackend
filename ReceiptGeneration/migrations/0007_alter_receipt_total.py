# Generated by Django 4.0 on 2023-05-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceiptGeneration', '0006_alter_receipt_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
