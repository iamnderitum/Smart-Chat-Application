"""
Views for the user API.
"""
from rest_framework import generics
from userprofile.serializers import (
    UserDetailsSerializer,
)
from userprofile.models import (
    UserDetails
)


class CreateUserDetailView(generics.CreateAPIView):
    """Create a new user Detail in the system."""
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()
