# Generated by Django 4.0 on 2023-04-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0020_remove_account_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='admin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]