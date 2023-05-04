from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.DecimalField(max_digits=6, decimal_places=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(
        "MenuItem",
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        "Ingredient",
        on_delete=models.CASCADE,
    )
    quantity = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self) -> str:
        return f'Menu Item:{self.menu_item} requires ingredient: {self.ingredient}'

class Purchase(models.Model):
    menu_item = models.ForeignKey(
        "MenuItem",
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'Menu Item: {self.menu_item} purchase as {self.timestamp}'
    
