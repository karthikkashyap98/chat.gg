from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.index),
    path('<str:room_name>/', views.room, name='room'),
    path('home/', views.home),
]
