from django.test import TestCase
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Room, Message


User = get_user_model()
class MessageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="12345")
        self.room = Room.objects.create(name="Test Room", description="This is a test Room")

    def test_create_message(self):
        message = Message.objects.create(
            room=self.room,
            user=self.user,
            content="This is a Test Message"
        )
        self.assertEqual(message.room, self.room)
        self.assertEqual(message.user, self.user)
        self.assertEqual(message.content, "This is a Test Message")


"""
    def test_message_str(self):
        message = Message.objects.create(
            room=self.room,
            user=self.user,
            content="This is another test message"
        )
        self.assertEqual(str(message), "This is another test")
"""
