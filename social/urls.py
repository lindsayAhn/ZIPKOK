from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('around', views.around, name='around'),
    path('art', views.art, name='art'),
    path('craft', views.craft, name='craft'),
    path('workout', views.workout, name='workout'),
    path('musicdance', views.musicdance, name='musicdance'),
    path('instrument', views.instrument, name='instrument'),
    path('cook', views.cook, name='cook'),
    path('homecafe', views.homecafe, name='homecafe'),
    path('movies', views.movies, name='movies'),
    path('books', views.books, name='books'),
    path('etc', views.etc, name='etc'),
    path('accountform', views.accountform, name='accountform'),
    path('recommendation', views.recommendation, name='recommendation'),
]