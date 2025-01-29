from django.shortcuts import render, redirect, get_object_or_404
from .forms import TattooForm
from .models import Tattoo, Categoria

def menu(request):
    return render(request, 'menu.html')

def acercade(request):
    return render(request, 'acercade.html')

def carrousel(request):
    return render(request, 'Carrousel.html')

def formulario(request):
    return render(request, 'registration/formulario.html')

def galeria(request):
    return render(request, 'galeria.html')

def login_view(request):
    return render(request, 'registration/login.html')

def tienda(request):
    tattoos=Tattoo.objects.all()
    categorias = Categoria.objects.filter(tattoo__isnull=False).distinct()
    return render(request, 'tienda.html', {'datos': tattoos, 'categorias': categorias})


def django_view(request):
    if request.method == 'POST':
        form = TattooForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o mostrar un mensaje de éxito
    else:
        form = TattooForm()

    return render(request, 'django.html', {'tattoo_form': form})


def form_tattoo(request):
    if request.method=='POST': 
        tattooForm = TattooForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('listado')
    else:
        tattooForm= TattooForm()
    return render(request, 'form_tattoo.html', {'tattoo_form': tattooForm})

def eliminar(request, id):
     tattooEliminado = Tattoo.objects.get(codigo=id)   #select * from tattoo where codigo=id
     tattooEliminado.delete()
     return redirect ('listado')

def modificar(request, id):
     tattooModificado=Tattoo.objects.get(codigo=id)
     datos = {
          'form' : TattooForm(instance=tattooModificado)
     }
     if request.method=='POST':
          formulario = TattooForm(data=request.POST, instance=tattooModificado)
          if formulario.is_valid:
               formulario.save()
               return redirect('listado')
     return render(request, 'modificar.html', datos)

def crear(request):
    if request.method=="POST":
        tattooform=TattooForm(request.POST,request.FILES)
        if tattooform.is_valid():
            tattooform.save()     #similar al insert en función
            return redirect ('otra')
    else:
        tattooform=TattooForm()
    return render (request, 'form_tattoo', {'tattooform': tattooform})

def listado(request):
	# accedemos al objeto que contiene los datos de la base
	# el método all traerá todos los tatuajes que estan en la tabla, es como el  select
	tattoos= Tattoo.objects.all()
	#ahora crearemos un diccionario donde pasaremos los datos del vehículo al template

	
	#ahora se agrega para enviarlo al template y se manda la variable datos que es donde queda el diccionario
	return render(request, 'listado.html',context={'datos':tattoos})
