from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField('IngredientThroughRecipe', related_name='recipes')
    instructions = models.TextField()
    # I'll add other fields as needed

    def __str__(self):
        return self.title

class IngredientThroughRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amount} {self.ingredient.name}"

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

