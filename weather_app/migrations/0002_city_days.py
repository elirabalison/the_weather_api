# Generated by Django 3.2.4 on 2021-07-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
