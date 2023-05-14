from django import forms

from .models import MenuItem, RecipeRequirement, Ingredient, Purchase


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class RecipeRequirementForm(forms.ModelForm):
    menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.all(), empty_label=None)
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), empty_label=None)

    class Meta:
        model = RecipeRequirement
        fields = "__all__"        

class PurchaseForm(forms.ModelForm):
    menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.all(), empty_label=None)

    class Meta:
        model = Purchase
        fields = ["menu_item", "paid"]
