from rest_framework import serializers
from i_18n_app.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title",)