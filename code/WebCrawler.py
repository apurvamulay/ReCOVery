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

    final_df.to_csv("../dataset/nytimes_dataset.csv")

def replace_publisher(old_csv, url, pub_name, new_csv):
    df2 = pd.read_csv(old_csv)
    df2['publisher'] = df2['publisher'].replace({url: pub_name}, regex=True)
    print(df2['publisher'])
    df2.to_csv(new_csv, index=False)


#get_articles("Enter API key")
#write_final_csv()

# replace_publisher("../dataset/news-dataset_cbs_news_old.csv", 'https://www.cbsnews.com', 'CBS News', '../dataset/news-dataset_cbs_news.csv')
# replace_publisher("../dataset/news-dataset_business_insider_old.csv", 'https://www.businessinsider.com', 'Business Insider', '../dataset/news-dataset_business_insider.csv')
# replace_publisher("../dataset/news-dataset_abc_news_old.csv", 'http[s]*://abcnews.go.com', 'ABC News', '../dataset/news-dataset_abc_news.csv')
# replace_publisher("../dataset/news-dataset_CNBC_old.csv", 'https://www.cnbc.com', 'CNBC', '../dataset/news-dataset_CNBC.csv')
# replace_publisher("../dataset/news-dataset_fiveThirtyEight_old.csv", 'https://fivethirtyeight.com', 'FiveThirtyEight', '../dataset/news-dataset_fiveThirtyEight.csv')
# replace_publisher("../dataset/news-dataset_npr_old.csv", 'https://www.npr.org', 'National Public Radio (NPR)', '../dataset/news-dataset_npr.csv')
# replace_publisher("../dataset/news-dataset_pbs_old.csv", 'https://www.pbs.org', 'PBS NewsHour', '../dataset/news-dataset_pbs.csv')
# replace_publisher("../dataset/news-dataset-reuters_old.csv", 'https://www.reuters.com', 'Reuters', '../dataset/news-dataset-reuters.csv')
# replace_publisher("../dataset/news-dataset-reuters.csv", 'http://widerimage.reuters.com', 'Reuters', '../dataset/news-dataset-reuters.csv')
#replace_publisher("../dataset/news-dataset_usa_today_old.csv", 'https://www.usatoday.com', 'USA Today', '../dataset/news-dataset_usa_today.csv')
#replace_publisher("../dataset/news-dataset_washington_monthly_old.csv", 'https://washingtonmonthly.com', 'Washington Monthly', '../dataset/news-dataset_washington_monthly.csv')
#replace_publisher("../dataset/news-dataset_yahoo_news_old.csv", 'https://news.yahoo.com', 'Yahoo! News', '../dataset/news-dataset_yahoo_news.csv')
#replace_publisher("../dataset/news_dataset_nytimes_old.csv", 'www.nytimes.com', 'The New York Times ', '../dataset/news_dataset_nytimes.csv')
#replace_publisher("../dataset/news-dataset_natural_news.csv", 'https://www.naturalnews.com', 'Natural News', '../dataset/news-dataset_natural_news.csv')
#replace_publisher("../dataset/news-dataset_natural_news.csv", 'https://naturalnewsblogs.com', 'Natural News', '../dataset/news-dataset_natural_news.csv')
#replace_publisher("../dataset/news-dataset_gateway_pundit.csv", 'https://www.thegatewaypundit.com', 'The Gateway Pundit', '../dataset/news-dataset_gateway_pundit.csv')