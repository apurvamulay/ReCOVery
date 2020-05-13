from urllib.parse import urlparse

from pynytimes import NYTAPI
import datetime
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup


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

    fp = open("api_response.json", "w+")
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
        fulltext = ''.join([fulltext, currentText])
    return fulltext


def write_final_csv():
    df = pd.read_json("api_response.json")
    print(df.columns)
    df['pub_name'] = df.apply(lambda x: extract_domain(x['web_url']), axis=1)

    df['body_text'] = df.apply(lambda x: get_body_text(x['web_url']), axis=1)

    final_df = df[['pub_name', 'web_url', 'headline', 'multimedia', 'body_text']]
    final_df.to_csv("nytimes_dataset.csv")


get_articles("Enter API key")
write_final_csv()
