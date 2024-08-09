from django.db import models
from base.models import BaseModel
from authentication.models import User, Profile


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
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE,

    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sender",
        blank=True,
        null=True
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receiver",
        blank=True,
        null=True
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]
        verbose_name_plural = "Message"

    def __str__(self):
        return f'{self.sender} - {self.receiver}'

    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile

    @property
    def receiver_profile(self):
        receiver_profile = Profile.objects.get(user=self.receiver)
        return receiver_profile
