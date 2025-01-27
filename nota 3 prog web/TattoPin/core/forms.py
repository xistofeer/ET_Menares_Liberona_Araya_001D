from django import forms
from django.forms import ModelForm
from .models import Tattoo, Categoria

class TattooForm(forms.ModelForm):
    class Meta: 
        model = Tattoo
        fields = [ 'codigo', 'titulo', 'tipo', 'categoria', 'imagen']
        labels = {
            'codigo': 'codigo',
            'titulo' : 'titulo',
            'tipo' : 'tipo',
            'categoria' : 'Categoria', 
            'imagen': 'Imagen'
        }
        widgets ={
            'codigo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control'
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese titulo..',
                    'id': 'titulo',
                    'class': 'form-control'
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese tipo..',
                    'id': 'tipo',
                    'class': 'form-control'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id': 'categoria',
                    'class': 'form-control'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
            
        }
