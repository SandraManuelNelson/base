from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import Template, Context 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def usuarios(request):
    context = {
        
    }
    return render(request, 'usuarios/usuarios.html', context)

def somos(request):        
    return render(request, "partials/somos.html")

def login_view(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('Tienda')
          
    
    return render(request, 'usuarios/login.html', {
        
    })
    
def logout_view(reques):
    logout(reques)
    messages.success(reques, 'Sesión cerrada exitosamente')
    return redirect('login')
