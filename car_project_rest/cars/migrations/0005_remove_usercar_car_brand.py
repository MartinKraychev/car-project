# Generated by Django 4.0.4 on 2022-05-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_usercar_car_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercar',
            name='car_brand',
        ),
    ]
