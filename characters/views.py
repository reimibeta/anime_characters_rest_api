from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Characters, Anime, Cosplays
from .serializers import CharactersSerializer, AnimeSerializer, CosplaySerializer

class CharactersView(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer
    permission_classs = (permissions.IsAuthenticatedOrReadOnly)

class AnimeView(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class CosplayView(viewsets.ModelViewSet):
    queryset = Cosplays.objects.all()
    serializer_class = CosplaySerializer