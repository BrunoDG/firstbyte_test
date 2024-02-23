from rest_framework import serializers
from .models import Recipe, Ingredient, Restaurant, IngredientThroughRecipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

class IngredientThroughRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientThroughRecipe
        fields = '__all__'
