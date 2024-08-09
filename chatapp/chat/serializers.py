from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import Room, Message

from authentication.serializers import ProfileSerializer


class MessageSerializer(serializers.ModelSerializer):
    receiver_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            "id",
            "user",
            "sender",
            "sender_profile",
            "receiver",
            "receiver_profile",
            "message",
            "is_read",
            "timestamp",
        ]


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'
