from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .sentiment_analysis import analyze_sentiment
from . recommendation_service import recommend_courses


import json
@login_required
def chat_view(request):
    return render(request, "basic_chat.html")

@csrf_exempt
def analyze_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message", "")

            #Perform Sentiment analysis
            sentiment_result = perform_sentiment_analysis(message)

            return JsonResponse({"sentiment": sentiment_result})
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid Json"}, status=400)

    return JsonResponse({"error":"Only POST Method allowed"}, status=405)

def perform_sentiment_analysis(message):
    # Dummy sentiment analysis function
    return 'positive' if 'good' in message else 'negative'

def recommend_view(request):
    user_id = request.user.id
    recommendations = recommend_courses(user_id)
    return JsonResponse({"recommendations": recommendations})
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

