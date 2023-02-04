from django.shortcuts import render, HttpResponse, redirect
from productos.models import Producto
from productos.carrito import Carrito
from django.db.models import Q

def listar_producutos(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) 
        ).distinct()  
    return render(request, "productos/tienda.html", {'productos':productos})

def tienda(request):    
    productos = Producto.objects.all()
    return render(request, "productos/tienda.html", {'productos':productos})

def inicio(request):    
    return render(request, "partials/inicio.html")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)    
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")