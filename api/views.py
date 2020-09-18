from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from api.models import Messages
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def new(request):
    return render(request, "new.html")


def index(request):
    if not request.user.is_authenticated:
        return redirect("/chat/login/")
    return render(request, 'chat/index.html', {"user": request.user})


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect("/chat/login/")
    messages = Messages.objects.filter(
        chat_room=room_name).order_by('id')[10:]
    print(messages)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user': request.user,
        'messages': messages
    })


def signin(request):
    print(request)
    if request.user.is_authenticated:
        print('auth')
        return redirect("chat/")
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print("Im in")
            login(request, user)
            return redirect("/chat/")
    return render(request, "signin.html")


def sign_out(request):
    logout(request)
    return redirect("/chat/")


def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_exists = User.objects.filter(username=username).exists()
        if not user_exists:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            login(request, user)
            return redirect("/chat/")
        else:
            return HttpResponse("User already exists. Try new username.")
    return render(request, "signup.html")
