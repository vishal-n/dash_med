from django.urls import path, include
from .views import sync_languages_to_db
from .views import get_existing_languages
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

urlpatterns = [
    path("", sync_languages_to_db, name='sync_up'),
    path("languages", get_existing_languages, name="get_languages")
]
