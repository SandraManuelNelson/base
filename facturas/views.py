from django.shortcuts import render, redirect
from facturas.models import Detalle_Factura
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

def factura(request):
    #return HttpResponse("Hola")
    productos = Detalle_Factura.objects.all()
    return render(request, "facturas/facturas.html", {'productos':Detalle_Factura})
