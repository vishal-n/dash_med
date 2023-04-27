import json
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
    article = Article.objects.get(id=2)
    languages_dict = {code: str(name) for code, name in settings.LANGUAGES}
    languages_json = json.dumps(languages_dict)
    print(f"{languages_json = }")
    article.title = languages_json
    article.save()
    return JsonResponse({"Hello": "World"}, status=status.HTTP_200_OK)
