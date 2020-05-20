from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSets,
    ValidationViewSets
)

router = routers.DefaultRouter()
router.register(r'user', UserViewSets)
urlpatterns = [
    path('', include(router.urls)),
    path(r'^auth/pay$', ValidationViewSets.as_view(), name='pay')
]
