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
from users import views as users_views


# The name in the urls path is for use it in the templates, with this name if yo need to change
# a url you can do it without to change the url in every part of the code, because you use the
# url name instead of the path
urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-word/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),

    path('posts/', posts_views.list_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For use just in development and serve the media
