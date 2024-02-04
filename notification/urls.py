from django.urls import path
from . import views

path('create_notification/', views.create_notification, name="create_notification"),
path('get_notification/', views.get_notification, name="get_notification"),
path('update_notification/', views.update_notification, name="update_notification"),