from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from authentication.models import CustomUser
from .forms import CreateChatForm
from .models import Chat, Message, UTC
# Create your views here.

@login_required
def get_chats(request):
    users = CustomUser.objects.filter(is_active=True, is_staff=False).exclude(
    id=request.user.id).order_by('date_joined')
    user = get_object_or_404(CustomUser, id=request.user.id)
    groups = Chat.objects.filter(members__in=[user], type=3)
    channels = Chat.objects.filter(members__in=[user], type=2)
    return render(request, 'chat_home.html', {'users': users, "groups": groups, "channels": channels})

@login_required
def create_channel_group(request):
    if request.method == 'POST':
        form = CreateChatForm(request.POST, user=request.user)
        if form.is_valid():
            chat = form.save()
            chat.members.add(request.user)
            user = get_object_or_404(CustomUser, id=request.user.id)
            chat.owner = user
            chat.save()
            return redirect('get_messages', chat_id=chat.id)
    else:
        form = CreateChatForm(user=request.user)

    return render(request, 'create_channel_group.html', {'form': form})

@login_required
def create_dm(request):
    member_id = request.GET.get("id", None)
    if member_id:
        member = CustomUser.objects.get(id=member_id)
        user = CustomUser.objects.get(id=request.user.id)
            # Check if a chat already exists between user and member
        if Chat.objects.filter(type=1, members__in=[user]).filter(members__in=[member]).exists():
            chat = Chat.objects.filter(type=1, members=user).filter(members=member).first()
            return redirect('get_messages', chat_id=chat.id)
        else:
            # Create a chat without saving it to the database yet
            chat = Chat.objects.create()
            # Set the many-to-many relationship using the set() method
            chat.members.set([user, member])
            # Save the chat to the database
            chat.save()
            return redirect('get_messages', chat_id=chat.id)
        

def delete_channel_group(request, chat_id):

    return render(request, 'chat_home.html')

def delete_dm(request, chat_id):

    return render(request, 'chat_home.html')

def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        message = Message(
            chat=chat,
            sender=request.user,
            content=request.POST.get('content'),
            created_at=datetime.now(UTC),
        )
        message.save()   

    return redirect('get_messages', chat_id=chat.id)

def get_messages(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'GET':
        user = get_object_or_404(CustomUser, id=request.user.id)
        chat = get_object_or_404(Chat, id=chat_id)
        messages = Message.objects.filter(chat__id=chat.id).order_by('created_at')

        if chat.type == 2:
            return render(request, 'channel_messages.html', {'chat_id':chat.id, 'chat_name': chat.get_chat_name(user), 'messages': messages, "is_channel": True, "is_owner": True if chat.owner == user else False})
        else:
            return render(request, 'chat_messages.html', {'chat_id':chat.id, 'chat_name': chat.get_chat_name(user), 'messages': messages})
    
    return redirect('get_messages', chat_id=chat.id)

def edit_message(request, chat_id, message_id):

    return redirect('get_messages', chat_id)

def delete_message(request, chat_id, message_id):

    return redirect('get_messages', chat_id)