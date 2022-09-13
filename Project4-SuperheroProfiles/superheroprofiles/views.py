from django.shortcuts import render
from django.views.generic import TemplateView


# Populate information to be sent to template
def populate_dict(path, name):
    bio = "BIO"
    strengths = "STRENGTHS"
    weaknesses = "WEAKNESSES"

    return {
        'photo_url': path,
        'hero_name': name,
        'bio': bio,
        'strengths': strengths,
        'weaknesses': weaknesses,
    }


# Create your views here.
class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {'photo_url': "nothing"}


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        hero_name = kwargs['name']
        image_path = f'/static/images/{hero_name}.jpg'
        return populate_dict(image_path, hero_name)
