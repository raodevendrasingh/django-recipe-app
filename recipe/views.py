from django.shortcuts import render

def recipe_view(request):
    return render(request, 'recipes.html')