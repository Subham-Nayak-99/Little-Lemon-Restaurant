# Generated by Django 5.0.7 on 2024-11-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_alter_order_token_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]