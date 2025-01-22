from django.db import models
from django.contrib.auth.models import User


# Tabla para tatuadores
class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del tatuador")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    profile_image = models.URLField(blank=True, verbose_name="Imagen de perfil")
    contact_info = models.TextField(blank=True, verbose_name="Información de contacto")
    
    def __str__(self):
        return self.name


# Tabla para tatuajes
class Tattoo(models.Model):
    id = models.CharField(max_length=4,primary_key=True,verbose_name="ID del tatuaje")
    title = models.CharField(max_length=100, verbose_name="Título del tatuaje")
    description = models.TextField(blank=True, verbose_name="Descripción")
    image_url = models.URLField(verbose_name="URL de la imagen")
    style = models.CharField(max_length=50, verbose_name="Estilo", blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tattoos")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")
    
    def __str__(self):
        return self.title


# Tabla para etiquetas (tags)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Etiqueta")

    def __str__(self):
        return self.name


# Relación muchos-a-muchos entre tatuajes y etiquetas
class TattooTag(models.Model):
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE, related_name="tattoo_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tattoo_tags")

    class Meta:
        unique_together = ("tattoo", "tag")


# Tabla para valoraciones
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(verbose_name="Puntuación", choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, verbose_name="Comentario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        unique_together = ("user", "tattoo")

    def __str__(self):
        return f"{self.user.username} - {self.rating}/5"


# Extensión de User (si es necesario)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorites = models.ManyToManyField(Tattoo, blank=True, related_name="favorited_by")

    def __str__(self):
        return self.user.username

