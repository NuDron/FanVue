from django.contrib import admin

from .models import Artist, Album, Genre

admin.site.register(Genre)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'genre')
    fields = ['name', 'bio', 'genre']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('rel_artist', 'name', 'release_date')
    fields = ['rel_artist', 'name']
