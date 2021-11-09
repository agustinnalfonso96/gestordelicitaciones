from django.contrib import admin
from gestorPedidos.models import Cliente, Articulo, Pedido, Licitacion, Anexo

# Register your models here.
class Cliente_Admin(admin.ModelAdmin):
    list_display = ("user","direccion","telefono")

class Licitacion_Admin(admin.ModelAdmin):
    list_display = ("numero","nombre","fecha_apertura")
    search_fields = ("numero","nombre","fecha_apertura")

class Articulo_Admin(admin.ModelAdmin):
    list_filter = ("seccion",)

class Pedido_Admin(admin.ModelAdmin):
    list_display = ("numero","fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

class Anexo_Admin(admin.ModelAdmin):
    list_display = ("nombre","archivo","licitacion","created_by")
    search_fields = ("nombre","archivo","licitacion","created_by")

admin.site.register(Cliente, Cliente_Admin)
admin.site.register(Licitacion,Licitacion_Admin)
admin.site.register(Anexo, Anexo_Admin)