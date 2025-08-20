from . import views
from django.urls import path

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),
    path('chats/<uri>/', views.ChatSessionView.as_view()),
    path('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),
]
