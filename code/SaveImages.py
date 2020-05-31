import requests
import pandas as pd
import numpy as np

df = pd.read_csv("../dataset/merged-files/recovery-news-data.csv")

count = 1


def get_image(image_url, news_id):
    print(image_url, news_id)
    if type(image_url) != float:
        image_url = image_url.replace('https', 'http')
        name = image_url.split('/')
        name = name[len(name) - 1]
        with open('../images/' + name, 'wb') as handle:
            response = requests.get(image_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                print(block)
                if not block:
                    break

                handle.write(block)


img = df.apply(lambda x: get_image(x['image'], x['news_id']), axis=1)
