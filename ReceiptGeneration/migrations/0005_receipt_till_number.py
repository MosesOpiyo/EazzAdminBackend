# Generated by Django 4.0 on 2023-05-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceiptGeneration', '0004_receipt_store_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='till_number',
            field=models.IntegerField(null=True),
        ),
    ]
