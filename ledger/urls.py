from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path("recipes/list", views.recipe_list, name="recipe_list"),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe_add"),
    path('recipe/<int:pk>/add_image/', RecipeImageCreateView.as_view(), name='recipe_add_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)