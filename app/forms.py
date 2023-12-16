from django import forms
from .models import Items  # Предположим, что ваша модель товара называется Product

class Items(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'info', 'price', 'author']