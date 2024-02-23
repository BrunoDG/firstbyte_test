from django.urls import path
from .views import RecipeListView, RecipeView, RestaurantListView, IngredientView, IngredientListView, IngredientThroughRecipeListView, IngredientThroughRecipeDetailView

urlpatterns = [
    path('recipe/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe-detail'),
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('ingredient/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>', IngredientView.as_view(), name='ingredient-detail'),
    path('ingredient-recipe/', IngredientThroughRecipeListView.as_view(), name='ingredient-recipe-list'),
    path('ingredient-recipe/<int:pk>/', IngredientThroughRecipeDetailView.as_view(), name='ingredient-recipe-detail'),
]
