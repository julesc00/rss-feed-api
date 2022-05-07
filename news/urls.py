from django.urls import path

from .views import list_news, scrape

app = "news"

urlpatterns = [
    path("scrape/", scrape, name="scrape"),
    path("", list_news, name="list-news"),
]
