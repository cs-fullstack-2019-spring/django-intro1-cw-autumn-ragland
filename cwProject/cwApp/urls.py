from django.urls import path

from . import views
# paths : choosing a path runs a function in the views folder
urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.music, name='music'),
    path('Ariana', views.ari, name='artist'),
    path('Chris', views.chris, name='artist'),
    path('King', views.king, name='artist'),
]
