from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RoomListCreate, RoomDetail, MessageListCreate, MessageViewSet, chat_view

router = DefaultRouter()
router.register(r"messages",MessageViewSet)

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("api/", include(router.urls)),
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('rooms/<int:room_pk>/messages/', MessageListCreate.as_view(), name='message-list-create'),
]
