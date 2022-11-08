"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hero.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),

    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/add', ArticleAddView.as_view(), name='article_add'),
    path('articles/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete',
         ArticleDeleteView.as_view(), name='article_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
    path('accounts/add/', UserAddView.as_view(), name='user_add'),

    path('photo/', PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/', PhotoEditView.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/carousel', PhotoCarouselView.as_view(), name='photo_carousel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
