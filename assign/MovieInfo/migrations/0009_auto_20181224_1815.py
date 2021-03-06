# Generated by Django 2.1.4 on 2018-12-24 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieInfo', '0008_auto_20181224_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['genre_name']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre_name',
        ),
        migrations.RenameField(
            model_name='subgenre',
            old_name='name',
            new_name='subgenre_name',
        ),
    ]
