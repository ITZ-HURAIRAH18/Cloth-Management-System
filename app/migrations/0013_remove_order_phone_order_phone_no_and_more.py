# Generated by Django 5.1.4 on 2025-01-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_phone_no_order_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='Phone_no',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
