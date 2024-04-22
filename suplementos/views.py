from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Marca, Suplemento, Categoria

# Create your views here.

def Home(request):
    return render(request, "suplementos/home.html")

def index(request):
    return render(request, "suplementos/index.html", {
        "suplementos": Suplemento.objects.all(),
        "categorias": Categoria.objects.all(),
        "marcas": Marca.objects.all(),
    })

def suplemento(request, id_suplemento):
    try:
        suplemento = Suplemento.objects.get(id=id_suplemento)
        return render(request, "suplementos/suplemento.html", {
            "suplemento": suplemento,
            "categorias": Categoria.objects.all(),
            "marcas": Marca.objects.all(),
        })
    except Suplemento.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

def agregar_suplemento(request):
    if request.method == "POST":
        id_marca = request.POST["marcaSuplemento"]
        nombreS = request.POST["nombreSuplemento"]
        sizeS = request.POST["sizeSuplemento"]
        precioS = int(request.POST["precioSuplemento"])
        descripcionS = request.POST["descripcionSuplemento"]
        imagenS = "/imagenes/"+request.POST["imagenSuplemento"]
        id_categoria = request.POST["categoriaSuplemento"]
        try:
            marcaS = Marca.objects.get(id=id_marca)
            categoriaS = Categoria.objects.get(pk=id_categoria)
            Suplemento.objects.create(marca=marcaS, nombre=nombreS, size=sizeS, precio=precioS, descripcion=descripcionS, imagen=imagenS, categoria=categoriaS)
            return HttpResponseRedirect(reverse("index"))
        except Categoria.DoesNotExist or Marca.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
    
def eliminar_suplemento(request, id_suplemento):
    if request.method == "POST":
        try:
            suplemento = Suplemento.objects.get(id=id_suplemento)
            suplemento.delete()
            return HttpResponseRedirect(reverse("index"))
        except Suplemento.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))

def modificar_suplemento(request, id_suplemento):
    if request.method == "POST":
        try:
            suplemento = Suplemento.objects.get(id=id_suplemento)
            id_marca = request.POST["marcaSuplemento"]
            suplemento.marca = Marca.objects.get(id=id_marca)
            suplemento.nombre = request.POST["nombreSuplemento"]
            suplemento.size = request.POST["sizeSuplemento"]
            suplemento.precio = int(request.POST["precioSuplemento"])
            suplemento.descripcion = request.POST["descripcionSuplemento"]
            imagenS = request.POST["imagenSuplemento"]
            if(imagenS and imagenS != None and imagenS != "" and imagenS!=suplemento.imagen):
                suplemento.imagen = imagenS
                suplemento.imagen =  "/imagenes/"+suplemento.imagen.url
            id_categoria = request.POST["categoriaSuplemento"]
            suplemento.categoria = Categoria.objects.get(pk=id_categoria)
            suplemento.save()
            return HttpResponseRedirect(reverse("index"))
        except Suplemento.DoesNotExist or Categoria.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
        
    
def categoria(request, id_categoria):
    try:
        categoria = Categoria.objects.get(id=id_categoria)
        return render(request, "suplementos/categoria.html", {
            "categoria": categoria
        })
    except Categoria.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    
def agregar_categoria(request):
    if request.method == "POST":
        nombreC = request.POST["nombreCategoria"]
        Categoria.objects.create(nombre=nombreC)
        return HttpResponseRedirect(reverse("index"))

def eliminar_categoria(request, id_categoria):
    if request.method == "POST":
        try:
            categoria = Categoria.objects.get(id=id_categoria)
            categoria.delete()
            return HttpResponseRedirect(reverse("index"))
        except Categoria.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
        except:
            return HttpResponseBadRequest("Hubo un error eliminando la categoria, asegurse de haber eliminado la categoria de todos los productos que puedan tenerla asignada.")
        
def modificar_categoria(request, id_categoria):
    if request.method == "POST":
        try:
            nombreC = request.POST["nombreCategoria"]
            categoria = Categoria.objects.get(id=id_categoria)
            categoria.nombre = nombreC
            categoria.save()
            return HttpResponseRedirect(reverse("index"))
        except Categoria.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
        
def suplementos_categoria(request, id_categoria):
    try:
        categoriaS = Categoria.objects.get(id=id_categoria)
        return render(request, "suplementos/suplementos_categoria.html", {
            "suplementos": Suplemento.objects.filter(categoria=categoriaS),
            "categoria": categoriaS,
        })
    except Categoria.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))



def marca(request, id_marca):
    try:
        marca = Marca.objects.get(id=id_marca)
        return render(request, "suplementos/marca.html", {
            "marca": marca
        })
    except Categoria.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    
def agregar_marca(request):
    if request.method == "POST":
        nombreM = request.POST["nombreMarca"]
        Marca.objects.create(nombre=nombreM)
        return HttpResponseRedirect(reverse("index"))

def eliminar_marca(request, id_marca):
    if request.method == "POST":
        try:
            marca = Marca.objects.get(id=id_marca)
            marca.delete()
            return HttpResponseRedirect(reverse("index"))
        except Marca.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
        except:
            return HttpResponseBadRequest("Hubo un error eliminando la marca, asegurse de haber eliminado la marca de todos los productos que puedan tenerla asignada.")
        
def modificar_marca(request, id_marca):
    if request.method == "POST":
        try:
            nombreM = request.POST["nombreMarca"]
            marca = Marca.objects.get(id=id_marca)
            marca.nombre = nombreM
            marca.save()
            return HttpResponseRedirect(reverse("index"))
        except Marca.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))

def suplementos_marca(request, id_marca):
    try:
        marcaS = Marca.objects.get(id=id_marca)
        return render(request, "suplementos/suplementos_marca.html", {
            "suplementos": Suplemento.objects.filter(marca=marcaS),
            "marca": marcaS,
        })
    except Marca.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))