import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
# from .sentiment_analysis import analyze_sentiment
# from . recommendation_service import recommend_courses


@login_required
def chat_view(request):
    return render(request, "chat.html")


class MessageListView(View):
    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class MsgCreateView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            serializer = MessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


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


"""
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
"""
