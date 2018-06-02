from django.contrib import admin
from productos.models import Producto,Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria',)
    list_display_links = list_display
    list_filter = ('categoria',)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)

# Register your models here.
