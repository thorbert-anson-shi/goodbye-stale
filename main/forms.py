from django import forms
from .models import Product
from django.utils.html import strip_tags


class ProductSuggestionForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    description = forms.Textarea()


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "ingredients", "category"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_ingredients(self):
        ingredients = self.cleaned_data["ingredients"]
        return strip_tags(ingredients)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)
