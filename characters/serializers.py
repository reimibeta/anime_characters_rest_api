from rest_framework import serializers
from .models import Characters, Anime, Cosplays

# class CharactersSerializer(serializers.ModelSerializer):
class CharactersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Characters
        fields = ('id', 'url', 'name', 'anime',)

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ('id','url','name')

class CosplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cosplays
        fields = ('id','url','name','characters')