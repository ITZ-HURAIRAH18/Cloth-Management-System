# Generated by Django 5.1.4 on 2025-01-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
