# Generated by Django 5.0.7 on 2024-10-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_cart_cartitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='menu_item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]