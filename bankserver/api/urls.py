from django.urls import path
from rest_framework import routers
from .views import (
    UserViewSets,
    ValidationViewSets
)

urlpatterns = [
    path('user/', UserViewSets),
    path('pay/', ValidationViewSets.as_view(), name='pay'),
]