from django.shortcuts import render, redirect
from .models import *

def home_page(request):
    return render(request, 'home-page.html')

def recipe_view(request):
    if request.method == 'POST':

        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipes.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        return redirect('/add-recipes/')
    
    queryset = Recipes.objects.all()

    context = {'recipes': queryset}
    
    return render(request, 'recipes.html', context)