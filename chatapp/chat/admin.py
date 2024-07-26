from django.contrib import admin
from .models import Room, Message

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room

    list_display = ("name", "description")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message

    list_display = ("room", "user", "content")

admin.register(Room, RoomAdmin)
admin.register(Message, MessageAdmin)