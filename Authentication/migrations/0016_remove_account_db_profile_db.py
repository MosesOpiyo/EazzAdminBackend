# Generated by Django 4.0 on 2023-03-30 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0010_remove_productdatabase_admins'),
        ('Authentication', '0015_account_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='db',
        ),
        migrations.AddField(
            model_name='profile',
            name='db',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.productdatabase'),
        ),
    ]
