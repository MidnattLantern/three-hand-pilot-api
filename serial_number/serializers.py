from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import SerialNumber


class SerialNumberSerializer(serializers.ModelSerializer):
    """ Docstring """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    user_authentication_id = serializers.ReadOnlyField(source='owner.user_authentication.id')
    updated_at = serializers.SerializerMethodField()
    display_link_product_name = serializers.CharField(source='link_product_name.product_name', read_only=True)
    display_link_partnering_end = serializers.CharField(source='link_partnering_end.partnering_end', read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    class Meta:
        """ Docstring """
        model = SerialNumber
        fields = [
            'id',
            'owner',
            'link_product_name',
            'link_partnering_end',
            'is_owner',
            'user_authentication_id',
            'updated_at',
            'serial_number',
            'display_link_product_name',
            'display_link_partnering_end',
        ]