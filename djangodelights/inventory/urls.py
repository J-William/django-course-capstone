from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingredients", views.IngredientView.as_view(), name="ingredients"),
    path(
        "ingredients/<int:pk>/delete",
        views.IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path("ingredients/create", views.IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("menu-items", views.MenuItemView.as_view(), name="menu-items"),
    path("menu-items/create", views.MenuItemCreateView.as_view(), name="menu-item-create"),
    path("menu-items/recipe-requirements/create", views.RecipeRequirementCreateView.as_view(), name='recipe-requirement-create'),
    path("purchases", views.PurchaseView.as_view(), name="purchases"),
    path("purchases/create", views.PurchaseCreateView.as_view(), name="purchase-create"),
    path("metrics", views.MetricsView.as_view(), name="metrics"),
]
