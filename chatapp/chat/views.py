from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
class MessageViewSet(viewsets.ModelViewSet):
    queryset=Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes=[IsAuthenticated]

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.queryset.filter(room_id=self.kwargs['room_pk'])

    def perform_create(self, serializer):
        room = Room.objects.get(pk=self.kwargs['room_pk'])
        serializer.save(room=room)

@login_required
def chat_view(request):
    return render(request, "basic_chat.html")