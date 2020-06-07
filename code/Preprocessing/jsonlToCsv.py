import numpy as np
import pandas as pd
import json_lines
import os.path
from os import path
import csv


if path.exists('../dataset/news_tweet_user.csv'):
    print("exists")
else:
    f = open('news_tweet_user.csv', 'w', newline='')
    headerNames = ['News_id', 'Tweet_id', 'User_id']
    writer = csv.DictWriter(f, fieldnames = headerNames)
    writer.writeheader()
    f.close()


writeFile = open('news_tweet_user.csv', 'a')
with open('../dataset/tweet-id-news.jsonl', 'rb') as f:
    for line in json_lines.reader(f, broken=True):
        news_id = str(line['news_id'])
        tweet_id = str(line['tweet']['id_str'])
        user_id = str(line['tweet']['user']['id_str'])
        print(news_id, tweet_id, user_id)
        entities = news_id+ "\t" + tweet_id + "\t" + user_id

        entities = entities.split("\t")
        writer = csv.writer(writeFile)
        writer.writerows([entities])
    writeFile.close()

