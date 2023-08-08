from .models import Cart, Option
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'