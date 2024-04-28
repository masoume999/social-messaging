from authentication.models import CustomUser
from enum import IntEnum
from datetime import datetime
from django.db import models
from uuid import uuid4
import pytz

UTC = pytz.UTC

CHAT_TYPES = [
	(1, "Direct Message"),
	(2, "Channel"),
	(3, "Group")
]

# Chat model with a many-to-many relationship to the default User model
class Chat(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=30, null=True)
    type = models.IntegerField(choices=CHAT_TYPES, default=1)
    members = models.ManyToManyField(CustomUser)  # Many-to-many relationship with default User model
    created_at = models.DateTimeField(default=datetime.now(UTC))
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='owned_chats')  # Many-to-one relationship with default User model

    def get_chat_name(self, requesting_user=None):
        if self.type in [2, 3] and self.name:
            return self.name
        elif self.type == 1 and self.members.exists() and requesting_user:
            # Assuming you want to use the username of the other member as the chat name
            other_member = self.members.exclude(pk=requesting_user.id).first()
            return other_member.username if other_member else 'Undefined Name'
        else:
            # Handle other cases if needed
            return 'Direct Message'

    def __str__(self):
        return self.get_chat_name()
    

class Message(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(UTC))

    def __str__(self):
        return self.content
