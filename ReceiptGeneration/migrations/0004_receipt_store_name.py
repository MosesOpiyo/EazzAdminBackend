# Generated by Django 4.0 on 2023-04-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceiptGeneration', '0003_alter_receipt_overseer'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='store_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]