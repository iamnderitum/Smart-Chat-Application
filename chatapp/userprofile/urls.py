from django.urls import path

from userprofile import views

urlpatterns = [
    path("create/", views.CreateUserDetailView.as_view(), name="create-userprofile"),
]
