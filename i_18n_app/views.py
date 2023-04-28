import json
import os
from django.shortcuts import render
from .models import Article
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from i_18n_app.serializers import ArticleListSerializer
from django.utils.translation import gettext_lazy as _


# Create your views here.
def get_existing_languages(request):
    articles = Article.objects.all()
    article_serializer = ArticleListSerializer(articles, many=True)
    articles = article_serializer.data
    return JsonResponse({"Response": articles}, status=status.HTTP_200_OK)


def sync_languages_to_db():
    article = Article.objects.get(id=2)
    languages_dict = {code: str(name) for code, name in settings.LANGUAGES}
    if languages_dict:
        languages_json = json.dumps(languages_dict)
    else:
        DEFAULT_LANGUAGES = (('en', _('English')),)
        default_languages_dict = {code: str(name) for code, name in DEFAULT_LANGUAGES}
        languages_json = json.dumps(default_languages_dict)
    print(f"{languages_json = }")
    article.title = languages_json
    article.save()
    return JsonResponse({"Response": "Success"}, status=status.HTTP_200_OK)
