from django.urls import path
from .import views
from usuarios.views import VRegistro, contacto

urlpatterns = [
    path('',views.usuarios,name="usuarios"), 
    path('registro',VRegistro.as_view(), name="registro"),          
    path('login',views.login_view,name="login"),           
    path('logout',views.logout_view,name="logout"), 
    path('contacto',views.contacto, name="Contacto"),          
]