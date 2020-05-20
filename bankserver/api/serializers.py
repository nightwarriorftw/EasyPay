from rest_framework import serializers
from bankserver.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('full_name', 'balance', 'PIN', 'upi_key')
        extra_kwargs = {'PIN': {'write_only': True}}


class ValidationSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    upi_key = serializers.CharField()
    PIN  = serializers.IntegerField()
    balance = serializers.FloatField()

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance
