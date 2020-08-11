

## ReCOVery

***The latest dataset paper with detailed analysis on the dataset can be found at [here](https://www.researchgate.net/publication/342093948_ReCOVery_A_Multimodal_Repository_for_COVID-19_News_Credibility_Research)***

This is the first version of the dataset and will be updated timely.

## Overview  

The complete dataset cannot be distributed because of Twitter privacy policies and news publisher copyrights.  Social engagements and user information are not disclosed because of Twitter Policy. The code in this repository can be used to download news articles from published websites and relevant social media data from Twitter. 

The repository contains 4 folders namely - code, dataset, features, and figure.

The dataset provided in this repository (located in `dataset` folder) includes the following files:

 - `recovery-news-data.csv` -  Samples of all news articles collected from 22 reliable and 38 unreliable websites 
 - `recovery-social-media-data.csv` -  Samples of social media information of news articles from the above websites

Each of the above CSV files is a comma-separated file and have the following respective columns:

1. recovery-news-data.csv
 - `news_id` - Unique identifier for each news article.
 - `url` - URL of the article from the website that published respective news. 
 - `publisher` - Publisher of the news article.
 - `author` - Author or authors of the article. This field is a list of names of authors separated by a comma.
 - `title` - Title of the news article.
 - `image` - The head image of the news article.
 - `body_text` - The complete body content of the news article.
 - `news_guard_score` - The score given by NewsGuard for the news source.
 - `mbfc_level` - Media Bias/Fact Check level for each news source.
 - `political_bias` - Political bias for each news source.
 - `country` - The country of the news publishing website.
 - `reliability` - reliability label of news article (1 = reliable, 0 = unreliable).
 
 2. recovery-social-media-data.csv
 - `news_id` - Unique identifier for each news article.
 - `tweet_id`- Unique identifier for every tweet.

`dataset/reliable-unreliable-news-sources.txt` contains a list of all the reliable and unreliable news websites used for the project.

## Installation    

###  Requirements:

 All the scripts are written in python and requires `python 3.6 +` to run.
 
 Twitter data is gathered using Twitter Developer account and API keys. The twitter developer account can be created at
 [https://developer.twitter.com/en]. Once the account is created, you can create the app. On successful creation of the app, the keys will be  available in the `keys and tokens` section of the app.
 
 To start using twitter APIs, add the keys to the `get_twitter_data.py` and run function set_creds(). This will add keys to the `code/credentials/api-credentials.yaml` file.
 
 Twitter data is gathered using premium search APIs.
 
 `code/collect_articles.ipynb` - The code to collect news articles from the news url.

Install all the libraries in `requirements.txt` using the following command
    
    pip install -r requirements.txt
   

## Reference
If you are using this dataset, please cite the following paper:
~~~~
@article{zhou2020repository,
  title={ReCOVery: A Multimodal Repository for COVID-19 News Credibility Research},
  author={Zhou, Xinyi and Mulay, Apurva and Ferrara, Emilio and Zafarani, Reza},
  journal={arXiv preprint arXiv:2006.05557},
  year={2020}
}
~~~~


