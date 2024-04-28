from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

# Create your models here.
class CustomUser(AbstractUser):
    # Add your custom fields here
    id = models.UUIDField(default=uuid4, primary_key=True)
    user_name = models.CharField(max_length=30, null=True)
    pass_word = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    bio = models.TextField(max_length=200, null=True)
