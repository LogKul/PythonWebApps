from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import *

# Create your views here.

# USER VIEWS


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


# HERO VIEWS
class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heroes'


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'


class HeroAddView(LoginRequiredMixin, CreateView):
    template_name = 'hero/add.html'
    model = Superhero
    fields = '__all__'


class HeroEditView(LoginRequiredMixin, UpdateView):
    template_name = 'hero/edit.html'
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'hero/delete.html'
    model = Superhero
    success_url = reverse_lazy('hero_list')


# ARTICLE VIEWS
class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'article'


class ArticleAddView(LoginRequiredMixin, CreateView):
    template_name = 'article/add.html'
    model = Article
    fields = ['title', 'content', 'photo']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, UpdateView):
    template_name = 'article/edit.html'
    model = Article
    fields = ['title', 'content', 'photo']


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article/delete.html'
    model = Article
    success_url = reverse_lazy('article_list')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'


class PhotoListView(ListView):
    template_name = 'photo/list.html'
    model = Photo
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoEditView(LoginRequiredMixin, UpdateView):
    template_name = 'photo/edit.html'
    model = Photo
    fields = '__all__'


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'photo/delete.html'
    model = Photo
    success_url = reverse_lazy('photo_list')


class PhotoCarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):

    def photo_data(id, image):
        x = dict(image_url=f"{image}", id=str(id), label=f"{image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, photo.photo) for id, photo in enumerate(photos)]
