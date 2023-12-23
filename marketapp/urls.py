from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from marketapp import views

urlpatterns = [
    path('categories/', views.add_ajax, name='get_categories')
]
