# Generated by Django 4.0 on 2023-03-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_remove_productdatabase_admin_productdatabase_admins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdatabase',
            name='admins',
        ),
        migrations.AddField(
            model_name='productdatabase',
            name='admin',
            field=models.IntegerField(null=True),
        ),
    ]
