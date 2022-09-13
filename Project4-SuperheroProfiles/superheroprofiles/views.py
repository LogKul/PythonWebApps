from django.shortcuts import render
from django.views.generic import TemplateView


# Populate information to be sent to template
def populate_dict(path, name):
    bio = "BIO"
    strengths = "STRENGTHS"
    weaknesses = "WEAKNESSES"

    if (name == "mob"):
        bio = "His name is Mob, from the tv series Mob Psycho 100. He cares about his friends, and only prefers to use his psychic powers when he really needs to. He\'s a special kid who just wants an ordinary life."
        strengths = {"1": "Incredible psychic power",
                     "2": "Kind and caring personality",
                     "3": "Works hard"}
        weaknesses = {"1": "Incredibly weak (physically)",
                      "2": "After using a large amount of psychic energy, needs to rest",
                      "3": "Refuses to use his powers when he doesn't have to"}
    elif (name == "wayne"):
        bio = "This is Wayne, from the games Hylics and Hylics 2. He lives in a clay world, full of incredibly verbose creatures, with an evil entity named Gibby trying to take over the world. Wayne fights with his friends to take back the world, and defeat the full moon, in order to bring peace back to his lands."
        strengths = {"1": "High physical attack",
                     "2": "\"Dissolution\" ability",
                     "3": "Can convert clay flesh to more health in the Afterlife"}
        weaknesses = {"1": "Not a lot of juice",
                      "2": "Not as strong without his teammates", }
    elif (name == "super monkey"):
        bio = "This is the Super Monkey from Bloons Tower Defense. It throws darts at an incredible speed in order to pop passing balloons, and is the most expensive base tower in the game due to its performance, even without upgrades. It can be upgraded into a Sun God, anti-Bloon plasma-shooting machine, or a batman-like shuriken thrower."
        strengths = {"1": "High damage output",
                     "2": "Can upgrade into strongest towers in the game",
                     "3": "Lot of flexibility in use-case"}
        weaknesses = {"1": "Can get overwhelmed by large clumps of bloons",
                      "2": "Expensive",
                      "3": "Some intermediary upgrades are useless"}
    elif (name == "golden seedling"):
        bio = "This is a Golden Seedling from the game Bug Fables. These quirky little creature are incredibly strong, as well as being very rare, and they drop Tangy Berries, of the the best items in the game! They can be found in the place of regular seedlings, or they are more prevalent around the Seedling Paradise."
        strengths = {"1": "Incredibly strong defense (only enemy to have per-hit, rather than flat damage)",
                     "2": "Incredible amount of damage, a force to be reckoned with",
                     "3": "Has the power of the Tangy Berry"}
        weaknesses = {"1": "Perishes to Leif's Ice Rain ability pretty easily",
                      "2": "Very scared, will run away for no reason",
                      "3": "Hunted because of their Tangy Berries"}
    elif (name == "little ghost"):
        bio = "This is the Little Ghost from Hollow Knight. He is a creature born of the void, and he has no thoughts or emotions. He is just a little ghost with a much larger role in the lands of Hallownest. He uses a nail to fight the bugs around him, and can weild the power of dreams and enter the mind of other bugs with a Dream Nail."
        strengths = {"1": "Very nimble, which allows it to strategically beat stronger opponents",
                     "2": "No mind to think, so he is not consumed by the Radiance",
                     "3": "Harnesses the power of the void, and can obtain many upgrades"}
        weaknesses = {"1": "Weak shell, so he can perish after only a few hits",
                      "2": "Is very small",
                      "3": "Can't talk"}

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
