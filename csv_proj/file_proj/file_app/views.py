from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import UserDetails


class UserListAPIView(APIView):
    def get(self, request, format=None):
        users = UserDetails.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)