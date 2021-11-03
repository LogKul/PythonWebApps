
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView
from .views_note import NoteView, NoteDeleteView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    path('',                            NoteView.as_view(),        name='home'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                  AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Note
    path('note/',                       NoteListView.as_view(),    name='note_list'),
    path('note/<int:pk>',               NoteDetailView.as_view(),  name='note_detail'),
    path('note/add',                    NoteCreateView.as_view(),  name='note_add'),
    path('note/<int:pk>/',              NoteUpdateView.as_view(),  name='note_edit'),
    path('note/<int:pk>/delete',        NoteDeleteView.as_view(),  name='note_delete'),

    # Chapter
    path('chapter/',                    ChapterListView.as_view(),    name='chapter_list'),
    path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/add',                 ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

]
