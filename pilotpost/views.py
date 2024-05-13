from rest_framework import generics, permissions, filters
from flynarc_api.permissions import IsOwnerOrReadOnly
from .models import PilotPost
from .serializers import PilotPostSerializer


class PilotPostList(generics.ListCreateAPIView):
    """ Docstring """
    serializer_class = PilotPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PilotPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PilotPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Docstring """
    serializer_class = PilotPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PilotPost.objects.all().order_by('-updated_at')
