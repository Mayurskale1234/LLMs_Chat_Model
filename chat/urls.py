
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('history/', views.chat_history, name='chat_history'),
]
