from django.urls import path
from . import views


urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('quotes/<int:pk>', views.quote_detail, name='quote_detail'),
    path('quotes/new', views.quote_create, name='quote_create'),
    path('quotes/<int:pk>/edit', views.quote_edit, name='quote_edit'),
    path('quotes/<int:pk>/delete', views.quote_delete, name='quote_delete'),
]