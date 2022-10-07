from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import *

# Create your views here.


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


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
