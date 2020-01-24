import datetime
import os
import re
from urllib.request import urlretrieve

import environ
import MySQLdb as _mysql
import requests
from bs4 import BeautifulSoup

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env.read_env(os.path.join(BASE_DIR, ".env"))
DB_NAME = env.db("DATABASE_URL").get("NAME")
DB_USER = env.db("DATABASE_URL").get("USER")
DB_PASSWORD = env.db("DATABASE_URL").get("PASSWORD")
DB_HOST = env.db("DATABASE_URL").get("HOST")
DB_PORT = env.db("DATABASE_URL").get("PORT")


def detailpage(soup):
    links = soup.find_all(class_="titleColumn")
    urls = [link.a["href"] for link in links]
    #    print(urls)
    for link in urls:
        detail_page = requests.get(f"{domain}{link}")
        soup = BeautifulSoup(detail_page.content, "html.parser")
        yield soup


domain = "https://www.imdb.com"
list_page = requests.get(f"{domain}/chart/top/?ref_=nv_mv_250")

soup = BeautifulSoup(list_page.content, "html.parser")
# print(soup)
regex = re.compile(r"\(\w+(\ +\w)?\)")
conn = _mysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
cursor = conn.cursor()
try:
    for content in detailpage(soup):
        try:
            result = content.find(class_="title_wrapper")
            movie_title = result.h1.get_text()
            movie_slug = movie_title.replace(" ", "-")
            release_text = result.find_all("a")[-1].get_text().strip()
            release_text = re.sub(regex, "", release_text)
            release_text = release_text.strip()
            print(release_text)
            release_date = datetime.datetime.strptime(release_text, "%d %B %Y")
            description = content.find(class_="summary_text").get_text().strip()
            imageUrl = content.find(class_="poster").a.img["src"]
            extensions = imageUrl.split(".")[-1]
            filename = f"src/media/movies/{movie_slug}.{extensions}"
            filepath = os.path.join(BASE_DIR, filename)
            urlretrieve(imageUrl, filepath)
            query = f"""
                INSERT INTO movies_movie (name, slug, release_date, description, image)
                VALUES (
                    "{movie_title}",
                    "{movie_slug}",
                    "{release_date}",
                    "{description}",
                    "{filename}"
                )"""
            cursor.execute(query)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
finally:
    conn.commit()
