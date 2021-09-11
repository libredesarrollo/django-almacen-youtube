from django import forms

from .models import Category

class ProductForm(forms.Form):
    title = forms.CharField(label="Título",max_length=255, min_length=3, required=True)
    description = forms.CharField(label="Descripción",required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20}))
    price = forms.FloatField(label="Precio",min_value=0.1)
    category = forms.ModelChoiceField(label="Categoría", queryset=Category.objects.all())