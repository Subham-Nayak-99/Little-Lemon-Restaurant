# Generated by Django 5.0.7 on 2024-11-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest_number',
            field=models.PositiveIntegerField(),
        ),
    ]