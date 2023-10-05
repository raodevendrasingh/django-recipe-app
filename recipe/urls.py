from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('delete-recipe/<int:id>/', views.delete_recipe, name='delete-recipe'),
    path('update-recipe/<int:id>/', views.update_recipe, name='delete-recipe')
]
