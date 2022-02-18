

## ReCOVery

***The final version of the latest dataset paper with detailed analysis on the dataset can be found at [here](https://www.researchgate.net/publication/342093948_ReCOVery_A_Multimodal_Repository_for_COVID-19_News_Credibility_Research)***


This is the first version of the dataset and will be updated timely.

## Overview  

The complete dataset cannot be distributed because of Twitter privacy policies and news publisher copyrights.  Social engagements and user information are not disclosed because of Twitter Policy. 

The dataset provided in this repository (located in `dataset` folder) includes the following files:

 - [`recovery-news-data.csv`](https://github.com/apurvamulay/ReCOVery/blob/master/dataset/recovery-news-data.csv) -  Samples of all news articles collected from 22 reliable and 38 unreliable websites 
 - [`recovery-social-media-data.csv`](https://github.com/apurvamulay/ReCOVery/blob/master/dataset/recovery-social-media-data.csv) -  Samples of social media information of news articles from the above websites

Each of the above CSV files is a comma-separated file and have the following respective columns:

1. recovery-news-data.csv
 - `news_id` - Unique identifier for each news article.
 - `url` - URL of the article from the website that published respective news. 
 - `publisher` - Publisher of the news article.
 - `publish_date` - The publishing date of the news article.
 - `author` - Author or authors of the article. This field is a list of names of authors separated by a comma.
 - `title` - Title of the news article.
 - `image` - The head image of the news article.
 - `body_text` - The complete body content of the news article.
 - `political_bias` - Political bias for each news source.
 - `country` - The country of the news source.
 - `reliability` - reliability label of the news article (1 = reliable, 0 = unreliable).
 
 2. recovery-social-media-data.csv
 - `news_id` - Unique identifier for each news article.
 - `tweet_id`- Unique identifier for every tweet.


## Installation    

###  Requirements:
 
 Twitter data is gathered using Twitter Developer account and API keys. The twitter developer account can be created at
 [https://developer.twitter.com/en]. Once the account is created, you can create the app. On successful creation of the app, the keys will be  available in the `keys and tokens` section of the app.
  
 Twitter data is gathered using premium search APIs.

[**Hydrator**](https://github.com/DocNow/hydrator) can be used to rehydrate Tweet ids

**Steps to Hydrate:**
1. Navigate to [hydrator](https://github.com/DocNow/hydrator) and follow readme OR download the installer from 
[hydrator executable](https://github.com/DocNow/hydrator/releases)
2. Run the installer and open the application 
3. Link the twitter account in the settings tab
4. In the dataset section, upload the file containing just the tweets. It will download csv with twitter information

## Reference
If you are using this dataset, please cite the following paper:
~~~~
@inproceedings{zhou2020recovery,
  title={ReCOVery: A Multimodal Repository for COVID-19 News Credibility Research},
  author={Zhou, Xinyi and Mulay, Apurva and Ferrara, Emilio and Zafarani, Reza},
  booktitle={Proceedings of the 29th ACM International Conference on Information \& Knowledge Management},
  pages={3205--3212},
  year={2020}
}
~~~~

## Contact
Please contact zhouxinyi@data.syr.edu if you have any question on the paper, data or the code.


