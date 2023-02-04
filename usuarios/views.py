from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.views.generic import View 
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm ,PasswordResetForm
from django.contrib import messages

class VRegistro(View):

    def get(self, request):
        form=SignUpForm( )
        return render(request,"usuarios/registro.html",{"form":form})

    def post(self, request):
        form=SignUpForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('inicio')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"usuarios/registro.html",{"form":form})



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
