from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ingredient, Restaurant, IngredientAmount
from .serializers import RecipeSerializer, IngredientSerializer, RestaurantSerializer, IngredientAmountSerializer

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

class IngredientAmountListView(generics.ListCreateAPIView):
    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer

class IngredientAmountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
