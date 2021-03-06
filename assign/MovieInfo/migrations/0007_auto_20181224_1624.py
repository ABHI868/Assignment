# Generated by Django 2.1.4 on 2018-12-24 16:24

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MovieInfo', '0006_auto_20181224_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='currency_currency',
            new_name='cost_currency',
        ),
        migrations.RemoveField(
            model_name='book',
            name='currency',
        ),
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='INR', max_digits=5),
        ),
    ]
