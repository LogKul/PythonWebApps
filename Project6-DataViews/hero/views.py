from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import *

# Create your views here.


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heroes'


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'


class HeroAddView(CreateView):
    template_name = 'hero/add.html'
    model = Superhero
    fields = '__all__'


class HeroEditView(UpdateView):
    template_name = 'hero/edit.html'
    model = Superhero
    fields = '__all__'


class HeroDeleteView(DeleteView):
    template_name = 'hero/delete.html'
    model = Superhero
    success_url = reverse_lazy('hero_list')
