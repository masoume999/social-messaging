from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.get_chats, name='chat_home'),
    path('create_channel_group/', views.create_channel_group, name="create_channel_group"),
    path('createdm/', views.create_dm, name="create_dm"),
    path('<uuid:chat_id>/send_message/', views.send_message, name='send_message'),
    path('<uuid:chat_id>/', views.get_messages, name='get_messages'),

    path('edit_message/', views.edit_message, name="edit_message"),
    path('delete_message/', views.delete_message, name="delete_message"),
]