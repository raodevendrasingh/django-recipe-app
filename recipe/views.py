from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model


def home_page(request):
    queryset = Recipes.objects.all()
    context = {'recipes': queryset}

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__contains=request.GET.get('search'))

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
        return redirect('/add-recipe/')

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


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            login_id=login_id
        )

        user.set_password(password)
        user.save()

        return redirect('/register')

    return render(request, 'register.html')
