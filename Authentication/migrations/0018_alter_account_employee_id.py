# Generated by Django 4.0 on 2023-04-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0017_remove_profile_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='employee_id',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
