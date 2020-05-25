import re

from wordcloud import WordCloud

import os
import pandas as pd
import nltk

from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Read stop-words file, stripe it to remove \n and store it in stopWords
stopWords_file = open("../dataset/stopWords.txt", "r", )
stopWords = stopWords_file.readlines()
stopWords = list(map(lambda s: s.lower().strip(), stopWords))



'''
Obtain the full records
'''
CSV_FILE_DIR_HEAD = "../"

CSV_FILE_DIR0 = CSV_FILE_DIR_HEAD + "dataset/reliable"
CSV_FILE_NAMES0 = os.listdir(CSV_FILE_DIR0)

dfs0 = pd.DataFrame()
for CSV_FILE_NAME in CSV_FILE_NAMES0:
    if CSV_FILE_NAME[:12] == "news-dataset":
        df = pd.read_csv(CSV_FILE_DIR0 + '/' + CSV_FILE_NAME)
        dfs0 = pd.concat([dfs0, df])

CSV_FILE_DIR1 = CSV_FILE_DIR_HEAD + "dataset/unreliable"
CSV_FILE_NAMES1 = os.listdir(CSV_FILE_DIR1)

dfs1 = pd.DataFrame()
for CSV_FILE_NAME in CSV_FILE_NAMES1:
    if CSV_FILE_NAME[:12] == "news-dataset":
        df = pd.read_csv(CSV_FILE_DIR1 + '/' + CSV_FILE_NAME)
        dfs1 = pd.concat([dfs1, df])

dfs = pd.concat([dfs0, dfs1])

'''
Obtain words within all titles and bodytexts
'''
words = ""


titles = dfs['title'].values
bodies = dfs['body_text'].values

for idx, title in enumerate(titles):
    if str(title) != 'nan':
        words += title
for idx, body in enumerate(bodies):
    if str(body) != 'nan':
        words += body

## remove stop words

text_tokens = word_tokenize(words.strip().lower())
tokens_without_sw = [word for word in text_tokens if not word in stopWords]
counter_words = nltk.Counter(tokens_without_sw)
tokens_without_sw_str = str(tokens_without_sw)


'''
Word Cloud
'''
data = WordCloud(background_color="white", max_words=200 )
data.generate(tokens_without_sw_str)
data.to_file(CSV_FILE_DIR_HEAD + 'figure/wordcloud.eps')