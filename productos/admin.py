from django.contrib import admin
from .models import Alfajor, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)

@admin.register(Alfajor)
class AlfajorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "relleno", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre", "relleno")