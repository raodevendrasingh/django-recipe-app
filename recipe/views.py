from django.shortcuts import render

# Create your views here.

def recipe_view(request):
    return render(request, 'recipes.html')