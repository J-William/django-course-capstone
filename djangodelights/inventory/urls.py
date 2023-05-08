from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingredients", views.IngredientView.as_view(), name="ingredients"),
    path(
        "ingredients/<int:pk>/delete",
        views.DeleteIngredientView.as_view(),
        name="ingredient-delete",
    ),
    path("menu-items", views.MenuItemView.as_view(), name="menu-items"),
    path("purchases", views.PurchaseView.as_view(), name="purchases"),
]
