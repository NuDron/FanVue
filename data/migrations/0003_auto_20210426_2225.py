# Generated by Django 3.2 on 2021-04-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210426_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.IntegerField(choices=[(7, 'Blues'), (2, 'Dance & Electro'), (0, '-'), (9, 'Lounge'), (3, 'Latin Music'), (6, 'Nu Metal'), (4, 'Alternative Rock'), (10, 'Funky'), (8, 'Elevator Music'), (5, 'Classic'), (1, 'Rock')], default=0, verbose_name='Genre'),
        ),
    ]
