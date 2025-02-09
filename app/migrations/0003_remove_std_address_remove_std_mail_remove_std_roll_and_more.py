# Generated by Django 5.1.4 on 2025-01-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_add_std_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='std',
            name='address',
        ),
        migrations.RemoveField(
            model_name='std',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='std',
            name='roll',
        ),
        migrations.AddField(
            model_name='std',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='std',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='std',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
