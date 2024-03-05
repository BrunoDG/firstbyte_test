from django.contrib import admin
from .models import Ingredient, IngredientAmount, Recipe, Restaurant

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Recipe)
admin.site.register(Restaurant)
