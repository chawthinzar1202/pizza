# Generated by Django 3.1.7 on 2021-04-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=64)),
                ('phone_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64)),
                ('item_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(default='defo', upload_to='images/'),
        ),
    ]
