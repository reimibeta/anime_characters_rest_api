from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters', views.CharactersView)
router.register('anime', views.AnimeView)
router.register('cosplays', views.CosplayView)
router.register('characterimages', views.CharacterImagesView)

urlpatterns = [
    path('', include(router.urls)),
]
