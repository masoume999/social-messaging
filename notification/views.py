from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from authentication.models import CustomUser
from .models import Chat, Message, Notification, UTC

def create_notification(request, chat_id, message_id):

    return ()

def get_notification(request, chat_id, message_id):

    return 

def update_notification(request, notification_id):

    return()