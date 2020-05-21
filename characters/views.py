from django.shortcuts import render
from rest_framework import viewsets
from .models import Characters
from .serializers import CharactersSerializer

class CharactersView(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer