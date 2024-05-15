from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from flynarc_api.permissions import IsOwnerOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """ Docstring """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all().order_by('-updated_at')
#    filter_backends = [
#        'owner__userauthentication',
#    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Docstring """
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.all().order_by('-updated_at')
