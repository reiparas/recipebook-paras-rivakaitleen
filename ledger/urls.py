from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list', views.recipe_list, name='recipe_list'),
    path('recipe/1', views.recipe1, name='recipe1'),
    path('recipe/2', views.recipe2, name='recipe2'),
]