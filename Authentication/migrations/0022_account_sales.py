# Generated by Django 4.0 on 2023-04-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0021_alter_account_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sales',
            field=models.IntegerField(null=True),
        ),
    ]
