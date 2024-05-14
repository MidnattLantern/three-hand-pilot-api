from rest_framework import serializers
from address_book.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """ Docstring """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        """ Docstring """
        model = Address
        fields = [
            'id',
            'owner',
            'is_owner',
            'updated_at',
            'partnering_end',
            'address_line1',
            'address_line2',
            'city',
            'postal_code',
            'contact_person_name',
            'contact_phone_number',
            'contact_email',
            'latitude',
            'longitude',
        ]
