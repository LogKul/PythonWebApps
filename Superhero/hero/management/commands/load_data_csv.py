from django.core.management.base import BaseCommand
from csv import reader
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

        path = Path('superhero_objects.csv')
        if path.exists():
            with open(path) as f:
                file_reader = reader(f)
                for row in file_reader:
                    Superhero.objects.get_or_create(
                        name=row[0], identity=row[1], description=row[2], strength=row[3], weakness=row[4], photo=row[5],)

            print("\nSuperhero objects loaded successfully!")
        else:
            print("ERROR: superhero_objects.csv could not be read.")
    elif user_input == "2":
        Article.objects.all().delete()

        path = Path('article_objects.csv')
        if path.exists():
            with open(path) as f:
                file_reader = reader(f)
                for row in file_reader:
                    Article.objects.get_or_create(
                        title=row[0], created_by=int(row[1]), created=row[2], modified=row[3], content=row[4],)

            print("\nArticle objects loaded successfully!")
        else:
            print("ERROR: superhero_objects.csv could not be read.")
