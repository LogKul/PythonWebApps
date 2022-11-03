from json import dump
from django.core.management.base import BaseCommand
from hero.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data()


def save_data():

    user_input = input(
        "Enter 1 to export superhero objects or 2 to export article objects: ")

    if user_input == "1":
        for hero in Superhero.objects.all().values():
            print(hero)

        data = [hero for hero in Superhero.objects.all().values()]

        with open('superhero_objects.json', "w") as f:
            dump(data, f, indent=4)

        print("\nSuperhero objects dumped to JSON successfully.")
    elif user_input == "2":
        for article in Article.objects.all().values():
            print(article)

        data = [article for article in Article.objects.all().values()]

        with open('article_objects.json', "w") as f:
            dump(data, f, indent=4, default=str)

        print("\nArticle objects dumped to JSON successfully.")
    else:
        print("Invalid input, script ending.")
