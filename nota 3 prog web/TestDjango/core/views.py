from django.shortcuts import render

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
