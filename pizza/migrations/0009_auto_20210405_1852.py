# Generated by Django 3.1.7 on 2021-04-05 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0008_auto_20210405_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProperOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('order_done', models.BooleanField(default=False)),
                ('order_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='priceofpizza',
            name='pizza',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='TypeOfPizza',
        ),
        migrations.DeleteModel(
            name='PriceOfPizza',
        ),
    ]