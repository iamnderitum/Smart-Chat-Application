"""
Views for the user API.
"""
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from authentication.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
