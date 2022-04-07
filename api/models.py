import uuid

from django.db import models


class Feed(models.Model):
    """Feed object."""
    title = models.CharField(max_length=255, db_index=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class Article(models.Model):
    """Article to be part of owned by a feed."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True)
    feed = models.ForeignKey(Feed, related_name="feeds", on_delete=models.CASCADE)
    url = models.URLField()
    summary = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(null=True, blank=True)
    date_read_by = models.CharField(max_length=255, blank=True, default="")
    loaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | Loaded: {str(self.loaded)}"


class ToggleRead(models.Model):
    """Toggle read for article read by user."""
    article_id = models.ForeignKey(Article, related_name="articles", on_delete=models.CASCADE)
    read_by_current_user = models.BooleanField(default=False)
