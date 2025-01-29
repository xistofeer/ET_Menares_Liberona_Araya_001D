# from disutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreCategoria


class Tattoo(models.Model):
    codigo= models.CharField(max_length=6, primary_key=True, verbose_name='codigo')
    titulo= models.CharField(max_length=20, verbose_name='titulo del tattoo')
    tipo = models.CharField(max_length=20, verbose_name='tipo de tattoo')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.FloatField(verbose_name='Precio')

    def __str__(self):
        return self.codigo