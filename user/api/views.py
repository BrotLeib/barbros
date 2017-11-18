from django.contrib.auth import get_user_model
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer


User = get_user_model()

class UserCreate(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
