from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from flynarc_api.permissions import IsOwnerOrReadOnly
from .models import Address
from .serializers import AddressSerializer


class AddressList(generics.ListCreateAPIView):
    """ Docstring """
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Address.objects.all().order_by('-updated_at')
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__userauthentication',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Docstring """
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Address.objects.all().order_by('-updated_at')