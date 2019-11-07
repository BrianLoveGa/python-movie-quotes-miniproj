from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('quotes', views.quote_list, name='quote_list'),
    path('quotes/<int:pk>', views.quote_detail, name='quote_detail'),
    path('quotes/new', views.quote_create, name='quote_create'),
    path('quotes/<int:pk>/edit', views.quote_edit, name='quote_edit'),
    path('quotes/<int:pk>/delete', views.quote_delete, name='quote_delete'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>', views.movie_detail, name='movie_detail'),
    path('movies/new', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit', views.movie_edit, name='movie_edit'),
    path('movies/<int:pk>/delete', views.movie_delete, name='movie_delete'),
    path("home/", views.home, name='home'),
]