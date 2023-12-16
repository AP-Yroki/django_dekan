from django import forms
from .models import Items

class Items(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'info', 'price', 'author']