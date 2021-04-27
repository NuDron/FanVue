# Generated by Django 3.2 on 2021-04-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='started',
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.IntegerField(choices=[(5, 'Classic'), (6, 'Nu Metal'), (0, '-'), (1, 'Rock'), (4, 'Alternative Rock'), (2, 'Dance & Electro'), (7, 'Blues'), (8, 'Elevator Music'), (3, 'Latin Music'), (10, 'Funky'), (9, 'Lounge')], default=0, verbose_name='Genre'),
        ),
    ]