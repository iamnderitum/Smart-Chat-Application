from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import chat_view, \
                   home, \
                   MessageViewSet, \
                   MessageListView, \
                   MsgCreateView, \
                   RoomListCreate, \
                   RoomDetail


router = DefaultRouter()
router.register(r"messages", MessageViewSet)

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("home/", home, name="home"),

    path("messages/", MessageListView.as_view(), name="message-list"),

    path('messages/create/', MsgCreateView.as_view(), name='message-create'),

    path("api/", include(router.urls)),
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
]
