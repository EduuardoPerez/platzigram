"""Platzigram URLs module"""

# Django
from django.contrib import admin
from django.conf import settings # This is for hack in development mode for serve the media
from django.conf.urls.static import static # This is for hack in development mode for serve the media
from django.urls import path

# Views into the configuration module
from platzigram import views as local_views

# Views from apps
from posts import views as posts_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-word/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For use just in development and serve the media
