"""Platzigram URLs module"""

# Django
from django.contrib import admin
from django.conf import settings # This is for hack in development mode for serve the media
from django.conf.urls.static import static # This is for hack in development mode for serve the media
from django.urls import path, include


# The name in the urls path is for use it in the templates, with this name if yo need to change
# a url you can do it without to change the url in every part of the code, because you use the
# url name instead of the path
urlpatterns = [

    path('admin/', admin.site.urls),

    # path('<route>', include(('<app>.<urls file>', '<app name>'), namespace='<namespace for the app route>'))
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For use just in development and serve the media
