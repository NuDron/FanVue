from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions, mixins, generics
from .models import Artist, Album, Genre
from .serializers import ArtistSerializer, AlbumSerializer


#################
#       API     #
#################

class ArtistViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # Set level of essential permissions.
    permission_classes = [permissions.IsAuthenticated]
    # Will be ordered by, and hyperlinked by.
    lookup_field = 'name'


class ArtistDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class AlbumDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    # Limits the methods allowed through API.
    http_method_names = ['get']
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # Set level of essential permissions.
    permission_classes = [permissions.IsAuthenticated]
    # Will be ordered by, and hyperlinked by.
    lookup_field = 'pk'


####################
#   Custom Views   #
####################

def home_view(request):
    genres = Genre.objects.all()

    return render(request,
                  'home_view.html',
                  context={
                      'genres': genres,
                  })


class genre_view(LoginRequiredMixin, View):

    def get(self, request, pk):
        # Create list of genres
        genres = Genre.objects.all()
        selected_genre = Genre.objects.get(pk=pk)
        artists = Artist.objects.filter(genre=selected_genre)
        print(selected_genre, artists)
        return render(request, 'genre_list.html',
                      context={
                          'l_menu': genres,
                          'content': artists,
                          'menu_cont': 'genre',
                          'pk': pk,
                      })


class art_view(LoginRequiredMixin, View):

    def get(self, request, pk):
        artists = Artist.objects.all()
        chosen_artist = Artist.objects.get(pk=pk)
        albums = chosen_artist.albums.all()
        return render(request, 'artist_list.html',
                      context={
                          'l_menu': artists,
                          'title': chosen_artist,
                          'content': albums,
                          'menu_cont': 'artist',
                      })


class album_view(LoginRequiredMixin, View):

    def get(self, request, pk):
        chosen_album = Album.objects.get(pk=pk)
        chosen_artist = Artist.objects.get(pk=chosen_album.rel_artist.pk)
        albums = chosen_artist.albums.all()
        return render(request, 'artist_list.html',
                      context={
                          'l_menu': albums,
                          'title': chosen_album,
                          'content': albums,
                          'menu_cont': 'album',
                      })
