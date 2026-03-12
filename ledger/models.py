from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    name = models.CharField(max_length=50)
    short_bio = models.TextField(
        validators=[MinLengthValidator(255)])

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipes",
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name}"


class RecipeImage(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_images"  # match your template
    )

    image = models.ImageField(upload_to="recipe_images/")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.recipe.name}"


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']  
    template_name = 'ledger/recipe_add_image.html'

    def form_valid(self, form):
        # Link image to correct recipe
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.kwargs['pk']})
