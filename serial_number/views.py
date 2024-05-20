from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from flynarc_api.permissions import IsOwnerOrReadOnly
from .models import SerialNumber
from .serializers import SerialNumberSerializer


class SerialNumberList(generics.ListCreateAPIView):
    """ Docstring """
    serializer_class = SerialNumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SerialNumber.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['link_product_name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SerialNumberDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Docstring """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SerialNumberSerializer
    queryset = SerialNumber.objects.all()
