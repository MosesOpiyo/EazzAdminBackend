# Generated by Django 4.0 on 2023-02-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_alter_account_shift_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='employee_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='shift_end',
            field=models.TimeField(null=True),
        ),
    ]
