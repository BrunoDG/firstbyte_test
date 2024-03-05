from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientAmount')
    instructions = models.TextField()

    def __str__(self):
        return self.title

class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount}g of {self.ingredient.name}"

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

