# Generated by Django 4.0 on 2023-02-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0011_account_confirm_end_shift_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='server_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
