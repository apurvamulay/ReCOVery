import pandas as pd
import os
import json


columns = ['mbfc_level', 'political_bias', 'country', 'reliability']
CSV_FILE_DIR_HEAD = "../"

REL_JSON_FILE = "reliable_web_statistics.json"
UNREL_JSON_FILE = "unreliable_web_statistics.json"

CSV_FILE_DIR_RELIABLE = CSV_FILE_DIR_HEAD + "dataset/reliable"
CSV_FILE_DIR_UNRELIABLE = CSV_FILE_DIR_HEAD + "dataset/unreliable"


def insert_statistics_columns(jsonfile, directory):
    CSV_FILE_NAMES = os.listdir(directory)
    with open(jsonfile) as json_file:
        data = json.load(json_file)

    for CSV_FILE_NAME in CSV_FILE_NAMES:
        if CSV_FILE_NAME[:12] == "news-dataset":
            fileName = directory + '/' + CSV_FILE_NAME
            print(fileName)
            df = pd.read_csv(fileName)
            pub = data[df['publisher'][0]]
            df['mbfc_level'] = pub['mbfc_level']
            df['political_bias'] = pub['political_bias']
            df['country'] = pub['country']
            df['reliability'] = pub['reliability']
            df.to_csv(fileName, index=False)


# Reliable websites
insert_statistics_columns(REL_JSON_FILE, CSV_FILE_DIR_RELIABLE)

# Unreliable websites
insert_statistics_columns(UNREL_JSON_FILE, CSV_FILE_DIR_UNRELIABLE)
