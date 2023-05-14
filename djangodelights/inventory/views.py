from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.db.models import Sum
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


def index(request):
    return render(request, "inventory/home.html")


class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
    context_object_name = "ingredients"

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingredients")

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingredients")

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_edit.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingredients")

class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"
    context_object_name = "menuitems"

class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create.html"
    context_object_name = "menuitems"
    form_class = MenuItemForm
    success_url = reverse_lazy("menu-items")

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create.html"
    context_object_name = "reciperequirements"
    form_class = RecipeRequirementForm
    success_url = reverse_lazy("menu-items")


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
    context_object_name = "purchases"

class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create.html"
    context_object_name = "purchases"
    form_class = PurchaseForm
    success_url = reverse_lazy("purchases")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.timestamp = timezone.now()
        # Calculate the cost of the MenuItem
        instance.cost = 0
        for req in instance.menu_item.recipe_requirements.all():
            instance.cost += req.ingredient.unit_price * req.quantity
        # Get the price for the menu item
        instance.paid = instance.menu_item.price
        instance.save()
        return super().form_valid(form)


class MetricsView(TemplateView):
    template_name = "inventory/metrics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_revenue"] = (
            round(Purchase.objects.aggregate(Sum("paid"))["paid__sum"], 2) or 0
        )
        context["total_cost"] = (
            round(Purchase.objects.aggregate(Sum("cost"))["cost__sum"], 2) or 0
        )
        context["total_profit"] = context["total_revenue"] - context["total_cost"]

        return context
