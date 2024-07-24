from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'editorial')  # Muestra los campos necesarios
    fields = ('titulo', 'autor', 'genero', 'editorial', 'descripcion', 'imagen')  

admin.site.register(Libro, LibroAdmin)
