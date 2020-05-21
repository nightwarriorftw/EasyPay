from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSets,
)
from bankserver.views import UpdateUserBalance

router = routers.DefaultRouter()
router.register(r'user', UserViewSets)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/pay', UpdateUserBalance, name='pay')
]
