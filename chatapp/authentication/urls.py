"""
URL mappings for the user API.
"""
from django.urls import path
from authentication import views
from authentication.views import (
    login,
    logout,
    AuthenticatedUser,
    PermissionAPIView
)
app_name = "authentication"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("me/", views.ManageUserView.as_view(), name="me"),

    path("login/", login, name="login"),
    path("user", AuthenticatedUser.as_view(), name="user"),
    path("logout/", logout, name="logout"),
    path("permissions/", PermissionAPIView.as_view(), name="permissions")
]
