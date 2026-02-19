from django.shortcuts import render

def recipe_list(request):
    recipes = [
        {"id": 1, "name": "Recipe 1"},
        {"id": 2, "name": "Recipe 2"},
    ]

    return render(request, "ledger/list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    recipes = {
        1: {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"},
            ]
        },
        2: {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2 cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"},
            ]
        }
    }

    recipe = recipes.get(recipe_id)

    return render(request, 'ledger/recipe_detail.html', {"recipe": recipe})