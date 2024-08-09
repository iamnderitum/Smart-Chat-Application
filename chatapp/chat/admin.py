from django.contrib import admin
from .models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room

    list_display = ("name", "description")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message

    list_display = ("sender", "receiver", "message", "timestamp")
