from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserTokenObtainPairSerializer


User = get_user_model()


class UserObtainTokenPairView(TokenObtainPairView):
    """Obtain authentication token for user"""
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer
