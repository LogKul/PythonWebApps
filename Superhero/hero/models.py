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
    photo = models.ImageField(
        upload_to='images', default='images/no_image.jpg')

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')


class Photo(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='images', default='images/no_image.jpg')

    def get_absolute_url(self):
        return reverse_lazy('photo_list')


class Article(models.Model):
    title = models.CharField(max_length=100, default="My Article")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField(default="Article body")
    photo = models.ForeignKey(
        Photo, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('article_list')

    class Meta:
        ordering = ['-modified']
