from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAuthentication
from .serializers import UserAuthenticationSerializer
from flynarc_api.permissions import IsOwnerOrReadOnly


class UserAuthenticationList(generics.ListAPIView):
    """ List view for all the user authentications """
#    def get(self, request):
#        users = UserAuthentication.objects.all()
#        serializer = UserAuthenticationSerializer(users, many=True)
#        return Response(serializer.data)
    serializer_class = UserAuthenticationSerializer
    queryset = UserAuthentication.objects.all().order_by('-created_at')


class UserAuthenticationDetail(generics.RetrieveUpdateAPIView):
    """ Retrieve or update user authentication """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UserAuthenticationSerializer
    queryset = UserAuthentication.objects.all().order_by('-created_at')
