# Generated by Django 4.0 on 2023-03-27 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0014_account_admin'),
        ('Products', '0003_alter_productdatabase_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdatabase',
            name='admin',
        ),
        migrations.AddField(
            model_name='productdatabase',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.account'),
        ),
    ]