from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

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


class Article(models.Model):
    title = models.CharField(max_length=100, default="My Article")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField(default="Article body")

    def get_absolute_url(self):
        return reverse_lazy('article_list')
