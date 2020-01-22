import os
from urllib.request import urlretrieve

import environ
import requests
from bs4 import BeautifulSoup

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env.read_env(os.path.join(BASE_DIR, ".env"))


def detailpage(soup):
    links = soup.find_all(class_="titleColumn")
    urls = [link.a["href"] for link in links]
    #    print(urls)
    for link in urls:
        detail_page = requests.get(f"{domain}{link}")
        soup = BeautifulSoup(detail_page.content, "html.parser")
        yield soup


# import mysqlclient
domain = "https://www.imdb.com"
list_page = requests.get(f"{domain}/chart/top/?ref_=nv_mv_250")

soup = BeautifulSoup(list_page.content, "html.parser")
# print(soup)
for content in detailpage(soup):
    result = content.find(class_="title_wrapper")
    movie_title = result.h1.get_text()
    movie_slug = movie_title.replace(" ", "-")
    release_text = result.find_all("a")[-1].get_text().replace("(India)", "").strip()
    description = content.find(class_="summary_text").get_text().strip()
    imageUrl = content.find(class_="poster").a.img["src"]
    extensions = imageUrl.split(".")[-1]
    filename = os.path.join(
        BASE_DIR, "src/media/movies/" + movie_slug + "." + extensions
    )
    urlretrieve(imageUrl, filename)
