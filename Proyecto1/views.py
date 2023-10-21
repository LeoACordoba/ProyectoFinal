from django.shortcuts import render
from users.models import Avatar

def inicio(request): #vista para inicio
    return render(request,'App1/inicio.html')