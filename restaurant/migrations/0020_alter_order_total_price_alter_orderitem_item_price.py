# Generated by Django 5.0.7 on 2024-11-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_alter_booking_guest_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]
