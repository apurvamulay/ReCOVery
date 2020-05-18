import pandas as pd
import os

df = pd.read_csv("../dataset/news-dataset_chicago_suntimes.csv", index_col=False)
remove_anonymous = ['Sun-Times Staff', 'Associated Press', 'Sun-Times Wire', 'Abigail Van Buren']


def get_val(authors):
    if type(authors) == str:
        string_auth = authors[1:len(authors) - 1]
        string_auth = string_auth.replace('\'', '')
        list_auth = string_auth.split(",")
        list_authors = []

        min_index = 100
        for index_val, value in enumerate(list_auth):
            if value.strip() in remove_anonymous:
                index = list_auth.index(value)
                if min_index > index:
                    min_index = index
        list_auth = list_auth[:min_index]

        for value in list_auth:
            j = value.strip()
            list_authors.append(j)

        return list_authors
    return authors


df['updated_authors'] = df.apply(lambda x: get_val(x['author']), axis=1)
df = df[~df.author.str.contains('Cst Editorial Board', na=False)]

df.to_csv("../dataset/news-dataset_chicago_suntimes.csv", index=False)


def update_indexes(fileName):
    df_fileName = pd.read_csv(fileName)
    df_fileName.set_index('url')
    df_fileName = df_fileName.drop('news_id', axis=1)
    df_fileName.index.name = 'news_id'
    fileName1 = fileName.rsplit("/")[2]
    print(fileName1)
    df_fileName.to_csv("../dataset/" + fileName1)


# Do not run this function
def read_files_from_directory():
    directory = os.path.join("/Users/apurvamulay/PycharmProjects/MIS-COV19/", "dataset/")
    print(directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            file = directory + file
            if file.endswith(".csv") and file.find("_old") == -1:
                f = open(file, 'r')
                update_indexes(file)
                #  perform calculation
                f.close()


files = ['news-dataset_abc_news.csv', "news-dataset_business_insider.csv", "news-dataset_cbs_news.csv",
         "news-dataset_chicago_suntimes.csv", "news-dataset_CNBC.csv", "news-dataset_fiveThirtyEight.csv",
         "news-dataset_npr.csv", "news-dataset_pbs.csv"]
for fileName in files:
    update_indexes("../dataset/" + fileName)
