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

class ValidationViewSets(APIView):
    
    def put(self, request, format=None):
        full_name = request.data['full_name']
        upi_key = request.data['upi_key']
        PIN = request.data['PIN']
        amount = request.data['amount']
        snippet = UserMode.objects.filter(
            full_name=full_name,
            upi_key = upi_key,
            PIN=PIN
        )
        if(snippet.balance >= amount):
            snippet.balance = snippet.balance-amount
        else:
            return Response({'details':'Insufficient Balance', 'status': '400'})
        serializer = ValidationSerializer()
        if serializer.is_valid():
            print(serializer.data)
            return Response({'details': 'success', 'status': '200'})
