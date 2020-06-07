import json
from datetime import datetime

import pandas as pd
from searchtweets import load_credentials
from searchtweets import gen_rule_payload
from searchtweets import ResultStream
import yaml

df = pd.read_csv("../dataset/recovery-news-data.csv")


# end point will be the API call you are trying to make
def set_creds():
    config = dict(
        search_tweets_api=dict(
            account_type='premium',
            endpoint='https://api.twitter.com/1.1/tweets/search/fullarchive/<environment-label>.json',
            consumer_key='Add your consumer key',
            consumer_secret='Add your consumer secret'
        )
    )

    with open('credentials/api-credentials.yaml', 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)

    premium_search_args = load_credentials("api-credentials.yaml",
                                           yaml_key="search_tweets_api",
                                           env_overwrite=False)
    print(premium_search_args)
    return premium_search_args


def get_twitter_results(news_id, query, from_date, premium_search_args, filename, to_date="202005260000"):
    query1 = "url:" + query + " lang:en"

    rule = gen_rule_payload(query1,
                            from_date=from_date,
                            to_date=to_date,
                            results_per_call=100)

    rs = ResultStream(rule_payload=rule,
                      max_results=100,
                      **premium_search_args)
    l = 0
    with open(filename, 'a', encoding='utf-8') as f:
        n = 0
        for tweet in rs.stream():
            news_tweet_json = {
                "news_id": news_id,
                "query": query,
                "tweet": tweet
            }

            n += 1
            if n % 10 == 0:
                print('{0}: {1}'.format(str(n), tweet['created_at']))
            json.dump(news_tweet_json, f)
            f.write('\n')
            l = datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +%f %Y").date()
    print(rs, type(l), l)
    print('done')
    return l


premium_search_args = set_creds()

fileName = "../../dataset/recovery-social-media-data.jsonl"
for index, row in df.iterrows():
    url = row['url'].replace('https://', '').replace('http://', '').replace(':', '')
    last_rec_date = get_twitter_results(row['news_id'], url,'202001210000', premium_search_args, fileName)
    while last_rec_date != 0 and last_rec_date != datetime.strptime('202001210000', '%Y%m%d%H%M').date():
        to_date = last_rec_date.strftime('%Y%m%d%H%M')
        last_rec_date = get_twitter_results(row['news_id'], url, '202001210000', premium_search_args, fileName,to_date)
