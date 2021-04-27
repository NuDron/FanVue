# Generated by Django 3.2 on 2021-04-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('bio', models.TextField(max_length=4096)),
                ('started', models.DateField(blank=True, verbose_name='Est.')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('genre', models.IntegerField(choices=[(3, 'Latin Music'), (2, 'Dance & Electro'), (4, 'Alternative Rock'), (5, 'Classic'), (8, 'Elevator Music'), (10, 'Funky'), (0, '-'), (6, 'Metal'), (1, 'Rock'), (7, 'Blues'), (9, 'Lounge')], default=0, verbose_name='Genre')),
                ('rel_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='data.artist')),
            ],
            options={
                'ordering': ['rel_artist', '-release_date', 'name'],
            },
        ),
    ]