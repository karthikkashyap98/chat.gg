from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.index),
    path('room/<str:room_name>/', views.room, name='room'),
    path('home/', views.home),
    path('login/', views.signin, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up),
]
