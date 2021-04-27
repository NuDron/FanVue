from rest_framework import serializers, pagination

from .models import Artist, Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'release_date']


class ArtistSerializer(serializers.ModelSerializer):
    requires_context = True
    art_albums = serializers.SerializerMethodField('get_art_albums')

    class Meta:
        model = Artist
        fields = ['name', 'art_albums']
        lookup_field = 'name'

    def get_art_albums(self, obj):
        my_albums = Album.objects.filter(rel_artist=obj)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(my_albums, self.context['request'])
        serializer = AlbumSerializer(page, many=True, context={'request': self.context['request']})
        print(serializer)
        return serializer.data
