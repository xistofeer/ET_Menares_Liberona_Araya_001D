from django.shortcuts import render, redirect, get_object_or_404
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


def eliminar(request, id):
    # Obtener el tatuaje por su ID y eliminarlo
    tattoo_eliminado = Tattoo.objects.get(id)
    tattoo_eliminado.delete()
    return redirect('menu')  # Cambia 'galeria' según el nombre de tu vista o página principal

def modificar(request, id):
    # Obtener el tatuaje por su ID para modificarlo
    tattoo_modificado = Tattoo.objects.get(id)
    datos = {
        'form': TattooForm(instance=tattoo_modificado)
    }
    if request.method == 'POST':
        formulario = TattooForm(data=request.POST, instance=tattoo_modificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('galeria')  # Cambia 'galeria' según el nombre de tu vista o página principal
    return render(request, 'modificar.html', datos)
    