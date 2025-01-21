from django.shortcuts import render, redirect
from .forms import TattooForm
from .models import Tattoo

def menu(request):
    return render(request, 'menu.html')

def acercade(request):
    return render(request, 'acercade.html')

def carrousel(request):
    return render(request, 'Carrousel.html')

def formulario(request):
    return render(request, 'formulario.html')

def galeria(request):
    return render(request, 'galeria.html')

def login_view(request):
    return render(request, 'login.html')


def django_view(request):
    if request.method == 'POST':
        form = TattooForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o mostrar un mensaje de éxito
    else:
        form = TattooForm()

    return render(request, 'django.html', {'tattoo_form': form})