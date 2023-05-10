from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.db.models import Sum

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientForm


def index(request):
    return HttpResponse("hello world")


class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
    context_object_name = "ingredients"


class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    form_class = IngredientForm
    success_url = "/"


class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"
    context_object_name = "menuitems"


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
    context_object_name = "purchases"


class MetricsView(TemplateView):
    template_name = "inventory/metrics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["total_revenue"] = Purchase.objects.aggregate(Sum("paid"))["paid__sum"] or 0
        context["total_cost"] = Purchase.objects.aggregate(Sum("cost"))["cost__sum"] or 0
        context["total_profit"] = context["total_revenue"] - context["total_cost"]

        return context