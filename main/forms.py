from django import forms
from .models import Product


class ProductSuggestionForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    description = forms.Textarea()


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "ingredients", "category"]
