# Generated by Django 5.0.7 on 2024-10-28 10:59

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_booking_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(default=datetime.time(14, 0)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be a valid number. E.g., '+919876543210' ", regex='^\\+?91?\\d{10}$')]),
        ),
    ]