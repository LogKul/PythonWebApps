from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class MobView(TemplateView):
    template_name = 'hero1.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Mob',
            'body': 'His name is Mob, from the tv series Mob Psycho 100.',
            'image': '/static/images/mob.jpg'
        }


class WayneView(TemplateView):
    template_name = "hero2.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Wayne',
            'body': 'This is Wayne, from the games Hylics and Hylics 2.',
            'image': '/static/images/wayne.jpg'
        }


class SuperMonkeyView(TemplateView):
    template_name = 'hero3.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Super Monkey',
            'body': 'This is the Super Monkey from Bloons Tower Defense.',
            'image': '/static/images/supermonkey.jpg'
        }
