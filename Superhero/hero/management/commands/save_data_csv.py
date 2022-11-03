from csv import writer
from django.core.management.base import BaseCommand
from hero.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data()


def save_data():

    user_input = input(
        "Enter 1 to export superhero objects or 2 to export article objects: ")

    if user_input == "1":

        data = [[hero.name, hero.identity, hero.description, hero.strength,
                 hero.weakness, hero.photo] for hero in Superhero.objects.all()]

        # CHANGE TO CSV
        with open('superhero_objects.csv', 'w', newline='') as f:
            writer(f).writerows(data)

        print("\nSuperhero objects dumped to CSV successfully.")
    elif user_input == "2":

        # data = [[article.title, article.created_by, article.created,
        #         article.modified, article.content] for article in Article.objects.all()]

        data = []
        for article in Article.objects.all().values():
            data += [[article["title"], int(article["created_by_id"]),
                      article["created"], article["modified"], article["content"]]]

        for row in data:
            print(row[0], row[1], row[2], row[3], row[4])

        # CHANGE TO CSV
        with open('article_objects.csv', 'w', newline='') as f:
            writer(f).writerows(data)

        print("\nArticle objects dumped to CSV successfully.")
    else:
        print("Invalid input, script ending.")
