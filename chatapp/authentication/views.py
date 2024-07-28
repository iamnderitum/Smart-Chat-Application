"""
Views for the user API.
"""
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from authentication.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
from authentication.models import User
from authentication.user_authenticate import (
    generateAccessToken,
    JWTAuthentication,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated User."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the Authenticated user."""
        return self.request.user

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed("User Not Found!")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect Password!")

    response = Response()

    token = generateAccessToken(user)
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {
        "jwt": token
    }
    return response

@api_view(["POST"])
def logout(_):
    response = Response()
    response.delete_cookie(key="jwt")
    response.data = {
        "message": "Success"
    }

    return response
class AuthenticatedUser(APIView):
    user = get_user_model()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({
            "data": serializer.data
        })