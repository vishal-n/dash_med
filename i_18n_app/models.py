from django.db import models


class Article(models.Model):
    title = models.JSONField("Article Title", default=dict)
