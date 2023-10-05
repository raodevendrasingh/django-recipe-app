from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='recipes'),
    path('add-recipes/', views.recipe_view, name='recipes')
]
