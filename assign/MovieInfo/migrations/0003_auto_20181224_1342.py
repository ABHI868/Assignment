# Generated by Django 2.1.3 on 2018-12-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieInfo', '0002_auto_20181224_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
