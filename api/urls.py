from django.urls import path, include
from api import views

urlpatterns = [
    path('home/', views.home)

]
