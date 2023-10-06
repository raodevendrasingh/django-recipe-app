from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('delete-recipe/<int:id>/', views.delete_recipe, name='delete-recipe'),
    path('update-recipe/<int:id>/', views.update_recipe, name='delete-recipe')
]
