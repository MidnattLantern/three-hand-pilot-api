from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ Docstring """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    
    class Meta:
        """ Docstring """
        model = Product
        fields = [
            'id',
            'owner',
            'is_owner',
            'updated_at',
            'product_name',
            'serial_number_prefix',
        ]
