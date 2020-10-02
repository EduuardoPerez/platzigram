"""Platzigram URLs module"""
from django.urls import path

# Views into the configuration module
from platzigram import views as local_views

# Views from apps
from posts import views as posts_views


urlpatterns = [
    path('hello-word/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts)
]
