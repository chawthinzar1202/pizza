# Generated by Django 3.1.7 on 2021-04-01 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20210401_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='item_id',
            new_name='pizza_id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='item_name',
            new_name='pizza_name',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='item_price',
            new_name='pizza_price',
        ),
    ]
