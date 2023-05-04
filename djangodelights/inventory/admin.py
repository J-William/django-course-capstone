from django.contrib import admin
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase

admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(MenuItem)
admin.site.register(Purchase)
