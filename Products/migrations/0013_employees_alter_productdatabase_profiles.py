# Generated by Django 4.0 on 2023-03-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_remove_productdatabase_access_allowed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='productdatabase',
            name='profiles',
            field=models.ManyToManyField(to='Products.Employees'),
        ),
    ]
