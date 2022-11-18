
from django.urls import path

from .views_hero import SuperheroDeleteView, SuperheroDetailView, SuperheroListView, SuperheroCreateView, SuperheroUpdateView


urlpatterns = [

    # Superhero
    path('hero/',                       SuperheroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',               SuperheroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                    SuperheroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',              SuperheroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',        SuperheroDeleteView.as_view(),  name='hero_delete'),

]
