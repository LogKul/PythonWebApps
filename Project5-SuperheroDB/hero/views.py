from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero


# Create your views here.
class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {'photo_url': "nothing"}


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        #image_path = f'/static/images/{hero_name}.jpg'
        return {
            'hero': Superhero.objects.get(pk=kwargs['pk'])
        }
