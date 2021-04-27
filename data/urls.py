from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .serializers import ArtistSerializer, AlbumSerializer
from .views import ArtistViewSet
from . import views

router = SimpleRouter()
router.register("api_artists", ArtistViewSet)

urlpatterns = [
    path('v1/', include((router.urls, 'api_v1'))),
    path('api_artist/<id>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('api_album/', views.AlbumDetail.as_view(), name='album_detail'),
    path('artist/<pk>/', views.art_view.as_view(), name='artist'),
    path('album/<pk>/', views.album_view.as_view(), name='album'),
    path('genre/<pk>/', views.genre_view.as_view(), name='genre'),
    path('', views.home_view, name='home'),
]