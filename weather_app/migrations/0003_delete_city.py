# Generated by Django 3.2.4 on 2021-07-01 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_city_days'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
