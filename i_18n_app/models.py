from django.db import models
from django.contrib import admin
from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from .forms import JSONFormField

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        # Add custom JSON encoding logic here
        return super().default(obj)

class Article(models.Model):
    title = models.JSONField("Article Title", default=dict, encoder=CustomJSONEncoder)

    def __str__(self) -> str:
        return self.title


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'form_class': JSONFormField},
    }

# admin.site.register(ArticleAdmin)
admin.site.register(Article, ArticleAdmin)
