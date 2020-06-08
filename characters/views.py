from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Characters, Anime, Cosplays, CharacterImages
from .serializers import CharactersSerializer, AnimeSerializer, CosplaySerializer, CharacterImagesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.request import Request
from django.http import Http404
from rest_framework import status

class CharactersView(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer
    # IsAuthenticatedOrReadOnly, IsAuthenticated
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = [JWTAuthentication,]

class CharacterImagesView(viewsets.ModelViewSet):
    queryset = CharacterImages.objects.all()
    serializer_class = CharacterImagesSerializer
    # permission_classes = (permissions.AllowAny,)

    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = [JWTAuthentication,]
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

class AnimeView(viewsets.ViewSet): #ModelViewSet,ViewSet
    # queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [JWTAuthentication,]
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # queryset = Anime.objects.all()
        anime = get_object_or_404(Anime, pk=pk)
        serializer = self.serializer_class(anime, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        # print('Request: {}'.format(request.data))
        instance = get_object_or_404(Anime, pk=pk)
        serializer = self.serializer_class(instance=instance,data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def partial_update(self, request, pk=None):
    #     pass
    #     return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(Anime, pk=pk)
        # self.destroy(instance)
        instance.delete()
        # serializer = self.serializer_class(instance,data=request.data, context={'request': request})
        # serializer = self.serializer_class(instance=instance, many=True, context={'request': request})
        # return Response(serializer.data)
        return Response({'details':{'item has been deleted.'}},status=status.HTTP_204_NO_CONTENT)
        # queryset = Anime.objects.all()
        # serializer = self.serializer_class(queryset, many=True, context={'request': request})
        # return Response(serializer.data)

class CosplayView(viewsets.ModelViewSet):
    queryset = Cosplays.objects.all()
    serializer_class = CosplaySerializer
