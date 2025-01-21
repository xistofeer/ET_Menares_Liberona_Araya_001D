from django.contrib import admin
from .models import Artist, Tattoo, Tag, TattooTag, Rating, UserProfile


# Configuración del modelo Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')  # Campos visibles en la lista
    search_fields = ('name',)  # Barra de búsqueda por nombre
    list_per_page = 20  # Paginación


# Configuración del modelo Tattoo
@admin.register(Tattoo)
class TattooAdmin(admin.ModelAdmin):
    list_display = ('title', 'style', 'artist', 'uploaded_at')  # Campos visibles en la lista
    list_filter = ('style', 'uploaded_at')  # Filtros laterales
    search_fields = ('title', 'description', 'artist__name')  # Barra de búsqueda
    autocomplete_fields = ('artist',)  # Autocompletado para artistas relacionados
    date_hierarchy = 'uploaded_at'  # Navegación jerárquica por fecha


# Configuración del modelo Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Campo visible en la lista
    search_fields = ('name',)  # Barra de búsqueda


# Configuración del modelo TattooTag
@admin.register(TattooTag)
class TattooTagAdmin(admin.ModelAdmin):
    list_display = ('tattoo', 'tag')  # Campos visibles en la lista
    search_fields = ('tattoo__title', 'tag__name')  # Barra de búsqueda


# Configuración del modelo Rating
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tattoo', 'rating', 'created_at')  # Campos visibles en la lista
    list_filter = ('rating', 'created_at')  # Filtros laterales
    search_fields = ('user__username', 'tattoo__title')  # Barra de búsqueda
    autocomplete_fields = ('user', 'tattoo')  # Autocompletado para usuarios y tatuajes


# Configuración del modelo UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Campo visible en la lista
    search_fields = ('user__username',)  # Barra de búsqueda
    filter_horizontal = ('favorites',)  # Widget para seleccionar favoritos


# Personalización del encabezado del sitio de administración
admin.site.site_header = "Administración de Galería de Tatuajes"
admin.site.site_title = "Admin Galería Tatuajes"
admin.site.index_title = "Gestión de Galería de Tatuajes"
