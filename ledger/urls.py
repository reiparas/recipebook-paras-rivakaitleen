from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'),

    path("password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset"),
    path("password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),
    path("reset_done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),

    path("recipes/list", views.recipe_list, name="recipe_list"),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
