# Generated by Django 4.0.4 on 2022-05-14 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_usercar_first_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercar',
            name='car_brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand'),
            preserve_default=False,
        ),
    ]
