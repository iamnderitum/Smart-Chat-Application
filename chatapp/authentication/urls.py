"""
URL mappings for the user API.
"""
from django.urls import path
from authentication import views

app_name = "authentication"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create")
]