from django.db import models

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.recipe_name


