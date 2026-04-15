
from django.shortcuts import render
from .models import Alfajor

def home(request):
    return render(request, "productos/home.html")

def alfajor(request):
    alfajores = Alfajor.objects.all().order_by("-id")
    return render(request, "productos/alfajor.html", {"alfajores": alfajores})