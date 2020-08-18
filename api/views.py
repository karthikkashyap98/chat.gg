from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "home.html")


def new(request):
    return render(request, "new.html")


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
