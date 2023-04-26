from django.db import models


class Article(models.Model):
    title = models.JSONField("Article Title", default=dict)

    def __str__(self) -> str:
        return self.title
