from django.db import models


class Genre(models.Model):
    genre = models.CharField('Genre', max_length=255)

    def __str__(self):
        return f'{self.genre}'


class Artist(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    bio = models.TextField(max_length=4096)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def get_albums(self):
        return self.albums.all()

    def get_name(self):
        return self.name


class Album(models.Model):
    rel_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=255)
    release_date = models.DateField(verbose_name='Release Date')

    class Meta:
        ordering = ['rel_artist', '-release_date', 'name']

    def __str__(self):
        return f'{self.name}, {self.release_date}'

    def get_name(self):
        return self.name

    def get_genres(self):
        return self.GENRE
