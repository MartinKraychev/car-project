# Generated by Django 4.0.4 on 2022-05-12 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carbrand_deleted_at_alter_carmodel_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercar',
            name='car_brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand'),
            preserve_default=False,
        ),
    ]
