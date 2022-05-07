import requests
from pprint import PrettyPrinter
from bs4 import BeautifulSoup as BSoup
import urllib3

from django.shortcuts import render, redirect

from .models import Headline


pp = PrettyPrinter(depth=3, indent=4)
urllib3.disable_warnings()


def scrape(request):
    """
    I have to rewire the tags since they spit nothing.
    """
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/breaking-news/news"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    pp.pprint(soup.prettify())
    news = soup.find_all("article", {"class": "cw4lnv-0 iTueKC js_post_item"})
    for article in news:
        main = article.find_all("a")[0]
        link = main.get("href")
        image_src = str(main.find("img").get("data-srcset")).split(" ")[-4]
        title = main.get("h2")
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
    return redirect("list-news")


def list_news(request):
    headlines = Headline.objects.all().order_by("-title")
    context = {
        "headlines": headlines
    }
    return render(request, "news/home.html", context)
