from django.db import models

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.name}'


class Strength(models.Model):
    hero = models.ForeignKey(Superhero, db_index=True,
                             on_delete=models.CASCADE)
    key = models.CharField(db_index=True, max_length=200)
    strength = models.TextField(db_index=True)


class Weakness(models.Model):
    hero = models.ForeignKey(Superhero, db_index=True,
                             on_delete=models.CASCADE)
    key = models.CharField(db_index=True, max_length=200)
    weakness = models.TextField(db_index=True)

# Superhero.objects.create(name='mob', bio='His name is Mob, from the tv series Mob Psycho 100. He cares about his friends, and only prefers to use his psychic powers when he really needs to. He\'s a special kid who just wants an ordinary life.', image='/static/images/mob.jpg')
# Strength.objects.create(hero_id=1, key='1', strength='Incredible psychic power')
# Strength.objects.create(hero_id=1, key='2', strength='Kind and caring personality')
# Strength.objects.create(hero_id=1, key='3', strength='Works hard')
# Weakness.objects.create(hero_id=1, key='1', weakness='Incredibly weak (physically)')
# Weakness.objects.create(hero_id=1, key='2', weakness='After using a large amount of psychic energy, needs to rest')
# Weakness.objects.create(hero_id=1, key='3', weakness='Refuses to use his powers when he doesn\'t have to')

# Superhero.objects.create(name='wayne', bio='This is Wayne, from the games Hylics and Hylics 2. He lives in a clay world, full of incredibly verbose creatures, with an evil entity named Gibby trying to take over the world. Wayne fights with his friends to take back the world, and defeat the full moon, in order to bring peace back to his lands.', image='/static/images/wayne.jpg')
# Strength.objects.create(hero_id=2, key='1', strength='High physical attack')
# Strength.objects.create(hero_id=2, key='2', strength='\"Dissolution\" ability')
# Strength.objects.create(hero_id=2, key='3', strength='Can convert clay flesh to more health in the Afterlife')
# Weakness.objects.create(hero_id=2, key='1', weakness='Not a lot of juice')
# Weakness.objects.create(hero_id=2, key='2', weakness='Not as strong without his teammates')
# Weakness.objects.create(hero_id=2, key='3', weakness='Perishes to Gibby\'s Big Bomb')

# Superhero.objects.create(name='super monkey', bio='This is the Super Monkey from Bloons Tower Defense. It throws darts at an incredible speed in order to pop passing balloons, and is the most expensive base tower in the game due to its performance, even without upgrades. It can be upgraded into a Sun God, anti-Bloon plasma-shooting machine, or a batman-like shuriken thrower.', image='/static/images/super monkey.jpg')
# Strength.objects.create(hero_id=3, key='1', strength='High damage output')
# Strength.objects.create(hero_id=3, key='2', strength='Can upgrade into strongest towers in the game')
# Strength.objects.create(hero_id=3, key='3', strength='Lot of flexibility in use-case')
# Weakness.objects.create(hero_id=3, key='1', weakness='Can get overwhelmed by large clumps of bloons')
# Weakness.objects.create(hero_id=3, key='2', weakness='Expensive')
# Weakness.objects.create(hero_id=3, key='3', weakness='Some intermediary upgrades are useless')

# Superhero.objects.create(name='golden seedling', bio='This is a Golden Seedling from the game Bug Fables. These quirky little creature are incredibly strong, as well as being very rare, and they drop Tangy Berries, of the the best items in the game! They can be found in the place of regular seedlings, or they are more prevalent around the Seedling Paradise.', image='/static/images/golden seedling.jpg')
# Strength.objects.create(hero_id=4, key='1', strength='Incredibly strong defense (only enemy to have per-hit, rather than flat damage)')
# Strength.objects.create(hero_id=4, key='2', strength='Incredible amount of damage, a force to be reckoned with')
# Strength.objects.create(hero_id=4, key='3', strength='Has the power of the Tangy Berry')
# Weakness.objects.create(hero_id=4, key='1', weakness='Perishes to Leif\'s Ice Rain ability pretty easily')
# Weakness.objects.create(hero_id=4, key='2', weakness='Very scared, will run away for no reason')
# Weakness.objects.create(hero_id=4, key='3', weakness='Hunted because of their Tangy Berries')

# Superhero.objects.create(name='little ghost', bio='This is the Little Ghost from Hollow Knight. He is a creature born of the void, and he has no thoughts or emotions. He is just a little ghost with a much larger role in the lands of Hallownest. He uses a nail to fight the bugs around him, and can weild the power of dreams and enter the mind of other bugs with a Dream Nail.', image='/static/images/little ghost.jpg')
# Strength.objects.create(hero_id=5, key='1', strength='Very nimble, which allows it to strategically beat stronger opponents')
# Strength.objects.create(hero_id=5, key='2', strength='No mind to think, so he is not consumed by the Radiance')
# Strength.objects.create(hero_id=5, key='3', strength='Harnesses the power of the void, and can obtain many upgrades')
# Weakness.objects.create(hero_id=5, key='1', weakness='Weak shell, so he can perish after only a few hits')
# Weakness.objects.create(hero_id=5, key='2', weakness='Is very small')
# Weakness.objects.create(hero_id=5, key='3', weakness='Can\'t talk')
