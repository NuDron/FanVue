# Generated by Django 3.2 on 2021-04-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=255, verbose_name='Genre'),
        ),
    ]
