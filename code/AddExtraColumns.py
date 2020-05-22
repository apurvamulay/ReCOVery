import pandas as pd
import os
import json

columns = ['news_guard_score', 'mbfc_level', 'political_bias']
CSV_FILE_DIR_HEAD = "../"

with open('reliable_web_statistics.json') as json_file:
    data = json.load(json_file)


print(data)
CSV_FILE_DIR0 = CSV_FILE_DIR_HEAD + "dataset/reliable"
CSV_FILE_NAMES0 = os.listdir(CSV_FILE_DIR0)


for CSV_FILE_NAME in CSV_FILE_NAMES0:
    if CSV_FILE_NAME[:12]=="news-dataset":
        fileName = CSV_FILE_DIR0 + '/' + CSV_FILE_NAME
        print(fileName)
        df = pd.read_csv(fileName)
        pub = data[df['publisher'][0]]
        df['news_guard_score'] = pub['news_guard_score']
        df['mbfc_level'] = pub['mbfc_level']
        df['political_bias'] = pub['political_bias']
        df.to_csv(fileName, )
