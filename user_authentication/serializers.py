from rest_framework import serializers
from .models import UserAuthentication


class UserAuthenticationSerializer(serializers.ModelSerializer):
    """ Serializer for User Authentication """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Meta """
        model = UserAuthentication
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',
        ]
