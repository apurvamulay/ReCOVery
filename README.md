

## ReCOVery

***The latest dataset paper with detailed analysis on the dataset can be found at [https://www.researchgate.net/publication/342093948_ReCOVery_A_Multimodal_Repository_for_COVID-19_News_Credibility_Research]***

This is the first version of the dataset and will be updated timely.

## Overview  

The complete dataset cannot be distributed because of Twitter privacy policies and news publisher copy rights.  Social engagements and user information are not disclosed because of Twitter Policy. The code in this repository can be used to download news articles from published websites and relevant social media data from Twitter. 

The repository contains 4 folders namely - code, dataset, features and figure

The dataset provided in this repository (located in `dataset` folder) include following files:

 - `recovery-news-data.csv` -  Samples of all news articles collected from 21 reliable and 38 unreliable websites 
 - `recovery-social-media-data.csv` -  Samples of social media information of news articles from above websites

Each of the above CSV files is comma separated file and have the following respective columns:

1. recovery-news-data.csv
 - `news_id` - Unique identifier for each news article.
 - `url` - Url of the article from website that published respective news. 
 - `publisher` - Publisher of the news article.
 - `author` - Author or authors of the article. This field is a list of names of authors separated by comma.
 - `title` - Title of the news article.
 - `image` - Head image of the news article.
 - `body_text` - The full body content of the news article.
 - `news_guard_score` - The score given by NewsGuard for the news source.
 - `mbfc_level` - Media Bias/Fact Check level for each news source.
 - `political_bias` - Political bias for each news source.
 - `country` - The country of the news publisher website.
 - `reliability` - reliability score of the news publisher (1 = reliable, 0 = unreliable).
 
 2. recovery-social-media-data.csv
 - `news_id` - Unique identifier for each news article.
 - `tweet_id`- Unique identifier for every tweet.

`dataset/reliable-unreliable-news-sources.txt` contains list of all reliable and unreliable news websites used for the project.

## Installation    

###  Requirements:

 All the scripts are writtern in python and requires `python 3.6 +` to run.
 
 The twitter data is gathered using Twitter Developer account and API keys. The twitter developer account can be created at
 [https://developer.twitter.com/en]. Once account is created, create the app. On successful creation of app, the keys will be  available in the `keys and tokens` section of the app.
 
 To start using twitter apis, add the keys to the `get_twitter_data.py` and run function set_creds(). This will add keys to  `api-credentials.yaml` file.
 
 The twitter data is gathered using premium search apis.

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


