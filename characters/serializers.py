from rest_framework import serializers
from .models import Characters, Anime, Cosplays, CharacterImages

# class CharactersSerializer(serializers.ModelSerializer):
class CharactersSerializer(serializers.HyperlinkedModelSerializer):
    # character_image = CharacterImagesSerializer(many=True)
    class Meta:
        model = Characters
        fields = ('id', 'url', 'name', 'anime')

class CharacterImagesSerializer(serializers.HyperlinkedModelSerializer):
    # characters = PrimaryKeyRelatedField(queryset=Characters.objects.all())
    class Meta:
        model = CharacterImages
        fields = ('id','url','image','character')

    def create(self, validated_data):
        return CharacterImages.objects.create(**validated_data)
    # def create(self, validated_data):
    #     """ Create and return a new user. """

    #     # character = Characters(
    #     #     email=validated_data['email'],
    #     #     name=validated_data['name'],
    #     #     raw_password=validated_data['raw_password'],
    #     # )

    #     # user.set_password(validated_data['password'])
    #     # user.save()

    #     return True

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ('id','url','name')

class CosplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cosplays
        fields = ('id','url','name','characters')