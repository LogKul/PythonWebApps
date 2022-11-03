from django.core.management.base import BaseCommand
from json import loads
from pathlib import Path
from hero.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()


def load_data():

    user_input = input(
        "Enter 1 to import superhero objects or 2 to import article objects: ")

    if user_input == "1":
        Superhero.objects.all().delete()

        path = Path('superhero_objects.json')
        if path.exists():
            objects = loads(path.read_text())

            # Generate objects from text file
            for object in objects:
                Superhero.objects.get_or_create(**object)

            # Display output to the console
            for hero in Superhero.objects.all().values():
                print(hero)

            print("\nSuperhero objects loaded successfully!")
        else:
            print("ERROR: superhero_objects.json could not be read.")
    elif user_input == "2":
        Article.objects.all().delete()

        path = Path('article_objects.json')
        if path.exists():
            objects = loads(path.read_text())

            # Generate objects from text file
            for object in objects:
                Article.objects.get_or_create(**object)

            # Display output to the console
            for article in Article.objects.all().values():
                print(article)

            print("\nArticle objects loaded successfully!")
        else:
            print("ERROR: superhero_objects.json could not be read.")
