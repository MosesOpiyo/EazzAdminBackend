# Generated by Django 4.0 on 2023-04-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceiptGeneration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='overseer',
            field=models.IntegerField(null=True),
        ),
    ]