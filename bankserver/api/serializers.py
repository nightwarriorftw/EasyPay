from rest_framework import serializers
from bankserver.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('full_name', 'balance', 'PIN', 'upi_key')
        extra_kwargs = {'PIN': {'write_only': True}}


class ValidationSerializer(serializers.Serializer):
    
    class Meta:
        model = UserModel
        
