# Generated by Django 4.0 on 2023-03-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_productdatabase_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdatabase',
            name='products',
            field=models.ManyToManyField(null=True, to='Products.Product'),
        ),
    ]
