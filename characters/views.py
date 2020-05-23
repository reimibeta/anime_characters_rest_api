from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Characters, Anime, Cosplays
from .serializers import CharactersSerializer, AnimeSerializer, CosplaySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CharactersView(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer
    # IsAuthenticatedOrReadOnly, IsAuthenticated
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication,]

class AnimeView(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CosplayView(viewsets.ModelViewSet):
    queryset = Cosplays.objects.all()
    serializer_class = CosplaySerializer
