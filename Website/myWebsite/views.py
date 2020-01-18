from django.shortcuts import render
from django.hhtp import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Salve, benvenuti, Vi trovate nella home principale.")
