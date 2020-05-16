import csv
from urllib.parse import urlparse

from pynytimes import NYTAPI
import datetime
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import dateutil.parser


def get_articles(api_key):
    nyt = NYTAPI(api_key)
    articles = nyt.article_search(
        query=['coronavirus', 'covid-19', 'sars-cov-2'],
        results=500,
        dates={
            "begin": datetime.datetime(2019, 11, 1)
        },
        options={
            "sources": [
                "New York Times"
            ]
        }
    )

    fp = open("../dataset/api_response.json", "w+")
    json.dump(articles, fp)


def extract_domain(url, remove_http=True):
    uri = urlparse(url)
    if remove_http:
        domain_name = f"{uri.netloc}"
    else:
        domain_name = f"{uri.netloc}://{uri.netloc}"
    return domain_name


def get_body_text(url):
    r1 = requests.get(url)
    coverpage = r1.content

    soup1 = BeautifulSoup(coverpage, 'html5lib')

    coverpage_news = soup1.find_all('div', class_='StoryBodyCompanionColumn')

    fulltext = ""
    for i in range(len(coverpage_news)):
        currentText = coverpage_news[i].get_text()
        fulltext = ''.join('\n').join([fulltext, currentText])
    return fulltext


def get_main_headline(headlines):
    return headlines['main']


def get_date(pub_date):
    return dateutil.parser.parse(pub_date).date()


def write_final_csv():
    df = pd.read_json("../dataset/api_response.json")
    df['publish_date'] = df.apply(lambda x: get_date(x['pub_date']), axis=1)

    df['publisher'] = df.apply(lambda x: extract_domain(x['web_url']), axis=1)

    df['body_text'] = df.apply(lambda x: get_body_text(x['web_url']), axis=1)
    df['title'] = df.apply(lambda x: get_main_headline(x['headline']), axis=1)
    df['image']  = df['multimedia']
    df['url'] = df['web_url']
    df['author'] = df['source']

    final_df = df[['url', 'publisher', 'publish_date', 'author', 'title', 'image', 'body_text']]
    final_df.index.name = 'news_id'

    final_df.to_csv("../dataset/nytimes_dataset.csv", quoting=csv.QUOTE_NONE, escapechar=' ')


get_articles("Enter API key")
write_final_csv()
