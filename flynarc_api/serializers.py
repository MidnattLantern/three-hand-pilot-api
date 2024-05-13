from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """ Docstring """
    user_authentication_id = serializers.ReadOnlyField(source='profile.id')
    user_authentication_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'user_authentication_id', 'user_authentication_image'
        )
