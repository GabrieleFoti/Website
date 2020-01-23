from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, "home.html")

def login(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(username = username, password = password)
    
    if user is not None:
        stuff = {
            "username" : user.username,
        }
        login(request, user)
        return render(request, "login.html", stuff)
    else:
        return HttpResponse("User not found")
