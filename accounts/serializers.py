from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            # 'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'phone': self.validated_data.get('phone', ''),
            'birthday': self.validated_data.get('birthday', ''),
            'address1': self.validated_data.get('address1', ''),
            'address2': self.validated_data.get('address2', ''),
            'address3': self.validated_data.get('address3', ''),
            'usertype': self.validated_data.get('usertype', ''),
            'profile': self.validated_data.get('profile', ''),
        }

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password1 = validated_data['password1'],
            password2 = validated_data['password2'],
            name = validated_data['name'],
            nickname= validated_data['nickname'],
            phone=validated_data['phone'],
            birthday=validated_data['birthday'],
            address1=validated_data['address1'],
            address2=validated_data['address2'],
            address3=validated_data['address3'],
            profile=validated_data['profile']
        )
        return user
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'name', 'nickname', 'phone', 'birthday', 'address1', 'address2', 'address3', 'profile', 'usertype')