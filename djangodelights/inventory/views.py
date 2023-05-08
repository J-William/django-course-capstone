from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientForm

def index(request):
    return HttpResponse('hello world')


class IngredientView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    form_class = IngredientForm
    success_url = '/'

class MenuItemView(ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    context_object_name ='menuitems'

class PurchaseView(ListView):
    model = Purchase
    template_name = 'PurchaseList.html'
    context_object_name = 'purchases'


