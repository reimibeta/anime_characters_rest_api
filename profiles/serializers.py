from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ A serializer for our user profile objects. """

    class Meta:
        model = UserProfile
        fields = ('id','url', 'email', 'name', 'password', 'raw_password')
        extra_kwargs = {
            'password': {'write_only': True},
            # 'raw_password': {'read_only': True}
        }

    def create(self, validated_data):
        """ Create and return a new user. """

        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
            raw_password=validated_data['raw_password'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
