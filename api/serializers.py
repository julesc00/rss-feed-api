
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from .models import Feed, Article


class UserTokenObtainPairSerializer(TokenObtainSerializer):
    """Serializer for the JWT token."""

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        token["username"] = user.username
        return token


class FeedSerializer(ModelSerializer):
    """Serializer for the Feed object."""

    class Meta:
        model = Feed
        fields = ("id", "title", "url")


class ArticleSerializer(serializers.Serializer):
    """Serializer for the Article object."""

    class Meta:
        model = Article
        fields = "__all__"


class NewArticleCountSerializer(serializers):
    new_article_count = serializers.IntegerField(min_value=0)


