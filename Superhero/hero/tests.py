from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import *


def user_args():
    return dict(username='TESTER', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class HeroDataTest(TestCase):

    def setUp(self):
        self.user = test_user()

    def test_add_test(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        Superhero.objects.create(
            name="a", identity="b", description="c", strength="d", weakness="e", image="f")
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, "a")
        self.assertEqual(x.identity, "b")
        self.assertEqual(x.description, "c")
        self.assertEqual(x.strength, "d")
        self.assertEqual(x.weakness, "e")
        self.assertEqual(x.image, "f")
        self.assertEqual(len(Superhero.objects.all()), 1)

    def test_test_edit(self):
        Superhero.objects.create(
            name="a", identity="b", description="c", strength="d", weakness="e", image="f")
        x = Superhero.objects.get(pk=1)
        x.name = 'herodude'
        x.save()
        self.assertEqual(x.name, 'herodude')
        self.assertEqual(len(Superhero.objects.all()), 1)

    def test_test_delete(self):
        Superhero.objects.create(
            name="a", identity="b", description="c", strength="d", weakness="e", image="f")
        b = Superhero.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Superhero.objects.all()), 0)


class ArticleDataTest(TestCase):

    def setUp(self):
        self.user = test_user()

    def test_add_test(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title="a", created_by=self.user, content="b")
        x = Article.objects.get(pk=1)
        self.assertEqual(x.created_by.username, "TESTER")
        self.assertEqual(x.title, "a")
        self.assertEqual(len(Article.objects.all()), 1)

    def test_test_edit(self):
        Article.objects.create(title="a", created_by=self.user, content="b")
        x = Article.objects.get(pk=1)
        x.title = 'newtitle'
        x.save()
        self.assertEqual(x.created_by.username, "TESTER")
        self.assertEqual(x.title, 'newtitle')
        self.assertEqual(len(Article.objects.all()), 1)

    def test_test_delete(self):
        Article.objects.create(title="a", created_by=self.user, content="b")
        b = Article.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Article.objects.all()), 0)


class HeroViewsTest(TestCase):

    def login(self):
        username = self.user.username
        password = user_args()['password']
        response = self.client.login(username=username, password=password)
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.hero = dict(name="a", identity="b", description="c",
                         strength="d", weakness="e", image="f")
        self.hero2 = dict(name="a2", identity="b2", description="c2",
                          strength="d2", weakness="e2", image="f2")

    def test_hero_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')

    def test_hero_list_view(self):
        self.assertEqual(reverse('hero_list'), '/')
        Superhero.objects.create(**self.hero)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')
        self.assertTemplateUsed(response, 'superhero_theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_hero_detail_view(self):
        Superhero.objects.create(**self.hero)
        self.assertEqual(reverse('hero_detail', args='1'), '/1')
        response = self.client.get(reverse('hero_detail', args='1'))
        self.assertContains(response, 'body')

    def test_hero_add_view(self):
        # Login to create Hero
        self.login()
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/add.html')

    def test_hero_edit_view(self):
        # Login to edit
        self.login()
        Superhero.objects.create(**self.hero2)
        response = self.client.post(
            reverse('hero_edit', args='1'), self.hero2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        superhero = Superhero.objects.get(pk=1)
        self.assertEqual(superhero.name, self.hero2['name'])

    def test_hero_delete_view(self):
        self.login()
        Superhero.objects.create(**self.hero)
        self.assertEqual(reverse('hero_delete', args='1'), '/1/delete')
        response = self.client.post('/1/delete')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Superhero.objects.all()), 0)


class ArticleViewsTest(TestCase):

    def login(self):
        username = self.user.username
        password = user_args()['password']
        response = self.client.login(username=username, password=password)
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.article = dict(title="a", content="b", created_by=self.user)
        self.article2 = dict(title="a2", content="b2", created_by=self.user)

    def test_article_home(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/list.html')

    def test_article_list_view(self):
        self.assertEqual(reverse('article_list'), '/articles/')
        Article.objects.create(**self.article)
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/list.html')
        self.assertTemplateUsed(response, 'superhero_theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_article_detail_view(self):
        Article.objects.create(**self.article)
        self.assertEqual(reverse('article_detail', args='1'), '/articles/1')
        response = self.client.get(reverse('article_detail', args='1'))
        self.assertContains(response, 'body')

    def test_article_add_view(self):
        # Login to create Hero
        self.login()
        response = self.client.get('/articles/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/add.html')

    def test_article_edit_view(self):
        # Login to edit
        self.login()
        Article.objects.create(**self.article2)
        response = self.client.post(
            reverse('article_edit', args='1'), self.article2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        article = Article.objects.get(pk=1)
        self.assertEqual(article.title, self.article2['title'])

    def test_article_delete_view(self):
        self.login()
        Article.objects.create(**self.article)
        self.assertEqual(reverse('article_delete', args='1'),
                         '/articles/1/delete')
        response = self.client.post('/articles/1/delete')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Article.objects.all()), 0)
