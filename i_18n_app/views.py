import os
from django.shortcuts import render
from .models import Article
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from i_18n_app.serializers import ArticleListSerializer

# Create your views here.
def get_existing_languages(request):
    articles = Article.objects.all()
    article_serializer = ArticleListSerializer(articles, many=True)
    articles = article_serializer.data
    return JsonResponse({"Response": articles}, status=status.HTTP_200_OK)

def sync_languages_to_db(request):
    articles = Article.objects.all()
    article_serializer = ArticleListSerializer(articles, many=True)
    articles = article_serializer.data
    languages = list(settings.LANGUAGES)
    for language in languages:
        language_code, language_name = language
        new_language_obj_to_be_added_to_db = Article(title={language_code: str(language_name)})
        new_language_obj_to_be_added_to_db.save()
    return JsonResponse({"Response": articles}, status=status.HTTP_200_OK)
