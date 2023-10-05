from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    queryset = Recipes.objects.all()
    context = {'recipes': queryset}
    return render(request, 'home-page.html', context)


def add_recipe(request):
    if request.method == 'POST':

        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipes.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect('/add-recipes/')

    return render(request, 'add_recipe.html')


def delete_recipe(request, id):
    queryset = Recipes.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_recipe(request, id):
    queryset = Recipes.objects.get(id=id)

    if request.method == 'POST':

        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/')

    context = {'recipes': queryset}
    return render(request, 'update_recipe.html', context)
