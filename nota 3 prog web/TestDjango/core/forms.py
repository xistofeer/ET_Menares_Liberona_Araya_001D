from django import forms
from django.forms import ModelForm
from .models import Tattoo, Artist

class TattooForm(forms.ModelForm):
    class Meta:
        model = Tattoo
        fields = ['title', 'description', 'image_url', 'style', 'artist']
        labels = {
            'title': 'Título del tatuaje',
            'description': 'Descripción',
            'image_url': 'URL de la imagen',
            'style': 'Estilo',
            'artist': 'Artista',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el título del tatuaje',
                    'id': 'title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción del tatuaje',
                    'id': 'description'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen',
                    'id': 'image_url'
                }
            ),
            'style': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el estilo del tatuaje',
                    'id': 'style'
                }
            ),
            'artist': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'artist'
                }
            ),
        }
