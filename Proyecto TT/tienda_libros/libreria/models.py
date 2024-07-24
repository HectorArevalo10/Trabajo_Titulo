from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    editorial = models.CharField(max_length=200)
    descripcion = models.TextField(default='Descripción no disponible')  # Valor predeterminado agregado
    imagen = models.ImageField(upload_to='imagenes_libros/', null=True, blank=True)

    def __str__(self):
        return self.titulo
