from rest_framework import serializers
from .models import Characters

class CharactersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Characters
        fields = ('id', 'name', 'anime',)