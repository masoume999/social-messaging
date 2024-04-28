from authentication.models import CustomUser
from enum import IntEnum
from datetime import datetime
from django.db import models
from uuid import uuid4
from messaging.models import Chat, Message
import pytz

UTC = pytz.UTC

class Notification(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now(UTC))
    members = models.ManyToManyField(CustomUser ,related_name='notifications_as_member')
    read_by = models.ManyToManyField(CustomUser, related_name='notifications_as_reader')

    def __str__(self):
        return self.id