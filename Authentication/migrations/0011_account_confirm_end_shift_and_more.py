# Generated by Django 4.0 on 2023-02-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0010_remove_account_shift_end_remove_account_shift_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='confirm_end_shift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='confirm_start_shift',
            field=models.BooleanField(default=False),
        ),
    ]
