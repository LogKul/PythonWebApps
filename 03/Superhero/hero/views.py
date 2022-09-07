from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class MobView(TemplateView):
    template_name = 'hero1.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Mob',
            'body': 'His name is Mob, from the tv series Mob Psycho 100. He cares about his friends, and only prefers to use his psychic powers when he really needs to. He\'s a special kid who just wants an ordinary life.',
            'image': '/static/images/mob.jpg'
        }


class WayneView(TemplateView):
    template_name = "hero2.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Wayne',
            'body': 'This is Wayne, from the games Hylics and Hylics 2. He lives in a clay world, full of incredibly verbose creatures, with an evil entity named Gibby trying to take over the world. Wayne fights with his friends to take back the world, and defeat the full moon, in order to bring peace back to his lands.',
            'image': '/static/images/wayne.jpg'
        }


class SuperMonkeyView(TemplateView):
    template_name = 'hero3.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Super Monkey',
            'body': 'This is the Super Monkey from Bloons Tower Defense. It throws darts at an incredible speed in order to pop passing balloons, and is the most expensive base tower in the game due to its performance, even without upgrades. It can be upgraded into a Sun God, anti-Bloon plasma-shooting machine, or a batman-like shuriken thrower.',
            'image': '/static/images/supermonkey.jpg'
        }
