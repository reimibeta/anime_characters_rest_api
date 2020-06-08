from django.urls import path, include
from . import views
from rest_framework import routers

# from .views import AnimeView

router = routers.DefaultRouter()
router.register('characters', views.CharactersView)
# Anime
# router.register('anime', views.AnimeView)
anime_list = views.AnimeView.as_view({'get':'list'})
anime_detail = views.AnimeView.as_view({'get':'retrieve'})
router.register(r'anime', views.AnimeView, basename='anime')

router.register('cosplays', views.CosplayView)
router.register('characterimages', views.CharacterImagesView)

urlpatterns = [
    path('', include(router.urls)),
]
