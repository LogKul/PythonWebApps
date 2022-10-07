from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=100, default="My Superhero")
    identity = models.CharField(max_length=100, default="No identity.")
    description = models.TextField(default="No description.")
    strength = models.CharField(max_length=100, default="No strengths.")
    weakness = models.CharField(max_length=100, default="No weaknesses.")
    image = models.CharField(max_length=100, default="No image url.")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')
