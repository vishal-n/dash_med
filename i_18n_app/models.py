from django.db import models
from django.contrib import admin
from django import forms
from .forms import JSONFormField

class Article(models.Model):
    title = models.JSONField("Article Title", default=dict)

    def __str__(self) -> str:
        return self.title


# class ArticleAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.JSONField: {'form_class': JSONFormField},
#     }

# admin.site.register(Article, ArticleAdmin)
