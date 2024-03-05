from django.urls import path
from .views import RecipeListView, RecipeView, RestaurantListView, IngredientView, IngredientListView, IngredientAmountListView, IngredientAmountDetailView

urlpatterns = [
    path('recipe/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe-detail'),
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('ingredient/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>', IngredientView.as_view(), name='ingredient-detail'),
    path('ingredient-amount/', IngredientAmountListView.as_view(),
         name='ingredient-amount-list'),
    path('ingredient-amount/<int:pk>/',
         IngredientAmountDetailView.as_view(), name='ingredient-amount-detail'),
]
