from django.contrib import admin
from usuarios.models import Municipio, Departamento, Categoria, Artesano

admin.site.site_header = 'ASOARTE STORE'

class AdminMunicipios(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    class Meta:
        model = Municipio

class AdminDepartamento(admin.ModelAdmin):
    list_display = ["nombre_departamento"]
    search_fields = ["nombre_departamento"]
    class Meta:
        model = Departamento


class AdminCategoria(admin.ModelAdmin):
	list_display = ["nombre"]
	search_fields = ["nombre"]
	class Meta:
		model = Categoria

class AdminArtesano(admin.ModelAdmin):
    list_display = ["nombre"]    
    class Meta:
        model = Artesano

admin.site.register(Artesano, AdminArtesano)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Municipio, AdminMunicipios)
admin.site.register(Departamento, AdminDepartamento)