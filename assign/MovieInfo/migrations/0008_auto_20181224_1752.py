# Generated by Django 2.1.4 on 2018-12-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieInfo', '0007_auto_20181224_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='subgenre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subgenre',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
