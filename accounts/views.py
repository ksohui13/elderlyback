from django.conf import settings
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework import permissions




# 회원가입
class UserCreate(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer