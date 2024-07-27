from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from authentication.models import User

class Room(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Message(BaseModel):
    room = models.ForeignKey(Room,
                             related_name='messages',
                             on_delete=models.CASCADE
                             )
    user = models.ForeignKey(User,
                             related_name='messages',
                             on_delete=models.CASCADE
                             )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.content[:20]}'
