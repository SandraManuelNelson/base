from django.contrib import admin
from productos.models import Producto, Devolucion

class AdminProducto(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    class Meta:
        model = Producto


class AdminDevolucion(admin.ModelAdmin):
    list_display = ["id_devolucion"]
    search_fields = ["id_devolucion"]
    class Meta:
        model = Devolucion

admin.site.register(Producto, AdminProducto)
admin.site.register(Devolucion, AdminDevolucion)
