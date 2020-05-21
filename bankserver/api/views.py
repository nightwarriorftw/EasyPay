from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response

from bankserver.models import UserModel
from .serializers import (
    UserSerializer,
    ValidationSerializer,
)

class UserViewSets(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class ValidationViewSets(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = (permissions.AllowAny,)

    def put(self, request, format=None):
        full_name = request.data['full_name']
        upi_key = request.data['upi_key']
        PIN = request.data['PIN']
        amount = request.data['amount']
        
        instance = self.get_object()
        if(instance.balance >= amount):
            instance.balance = instance.balance-amount
            instance.save()
            serializer = self.get_serializer(instance)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'details': 'success', 'status': '200'})
        else:
            return Response({'details':'Insufficient Balance', 'status': '400'})
        
