from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ingredient, Restaurant, IngredientThroughRecipe
from .serializers import RecipeSerializer, IngredientSerializer, RestaurantSerializer, IngredientThroughRecipeSerializer

# Create your views here.
class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class IngredientThroughRecipeListView(generics.ListCreateAPIView):
    queryset = IngredientThroughRecipe.objects.all()
    serializer_class = IngredientThroughRecipeSerializer

class IngredientThroughRecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IngredientThroughRecipe.objects.all()
    serializer_class = IngredientThroughRecipeSerializer
