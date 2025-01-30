from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import TattooForm
from .models import Tattoo, Categoria, Carrito

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

def carrito(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para ver tu carrito.")
        return redirect('login')

    carrito_items = Carrito.objects.filter(usuario=request.user)
    total_precio = sum(item.tattoo.precio for item in carrito_items)

    return render(request, 'carrito.html', {'carrito': carrito_items, 'total_precio': total_precio})

def agregar_al_carrito(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Debes iniciar sesión para agregar productos al carrito."}, status=403)

        tattoo_id = request.POST.get("tattoo_id")
        tattoo = get_object_or_404(Tattoo, id=tattoo_id)

        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        if carrito.productos.filter(id=tattoo.id).exists():
            return JsonResponse({"error": "Este producto ya está en el carrito."}, status=400)

        carrito.productos.add(tattoo)
        carrito.save()

        return JsonResponse({"message": "Producto agregado al carrito."})

    return JsonResponse({"error": "Método no permitido."}, status=405)

def eliminar_del_carrito(request, tattoo_id):
    if request.user.is_authenticated:
        tattoo = get_object_or_404(Tattoo, codigo=tattoo_id)
        carrito_item = Carrito.objects.filter(usuario=request.user, tattoo=tattoo).first()
        
        if carrito_item:
            carrito_item.delete()
            messages.success(request, "Tatuaje eliminado del carrito.")

    return redirect('carrito')

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
