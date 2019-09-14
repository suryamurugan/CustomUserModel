from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

from .models import User
from . import serializers

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

'''
class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer'''


'''
@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
        '''