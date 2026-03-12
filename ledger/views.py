from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Recipe, RecipeImage
from django.urls import reverse_lazy


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "ledger/list.html", context)


@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name"]
    template_name = "ledger/recipe_add.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "ledger/recipe_add_image.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.kwargs["pk"]})
