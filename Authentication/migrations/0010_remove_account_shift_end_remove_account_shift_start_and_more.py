# Generated by Django 4.0 on 2023-02-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0009_alter_account_employee_id_alter_account_shift_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='shift_end',
        ),
        migrations.RemoveField(
            model_name='account',
            name='shift_start',
        ),
        migrations.AddField(
            model_name='account',
            name='on_shift',
            field=models.BooleanField(default=False),
        ),
    ]