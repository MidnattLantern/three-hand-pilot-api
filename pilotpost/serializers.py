from rest_framework import serializers
from pilotpost.models import PilotPost


class PilotPostSerializer(serializers.ModelSerializer):
    """ Docstring """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    class Meta:
        model = PilotPost
        fields = [
            'id',
            'owner',
            'is_owner',
            'updated_at',
            'title',
            'image',
        ]