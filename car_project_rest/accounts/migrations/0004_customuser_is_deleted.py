# Generated by Django 4.0.4 on 2022-05-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
