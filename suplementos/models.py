from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"

class Marca(models.Model):
    nombre = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"

class Suplemento(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT, related_name="marca")
    nombre = models.CharField(max_length=64)
    size = models.CharField(max_length=8) #Peso, volumen, servicios, etc.
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=512, blank=True, default='')
    imagen = models.ImageField(upload_to="imagenes/")   #Como limitacion, las imagenes que se carguen deben estar en la carpeta /imagenes/ del proyecto para poder visualizarlas correctamente.
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, related_name="categoria")

    def __str__(self) -> str:
        return f"{self.marca.nombre} {self.nombre}, {self.categoria.nombre}, ${self.precio}"
