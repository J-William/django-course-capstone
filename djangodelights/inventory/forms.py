from django import forms

from .models import MenuItem, RecipeRequirement, Ingredient, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"