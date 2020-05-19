import pandas as pd
import os

df = pd.read_csv("../dataset/news-dataset_chicago_suntimes.csv", index_col=False)
remove_anonymous = ['Sun-Times Staff', 'Associated Press', 'Sun-Times Wire', 'Abigail Van Buren']


def get_list_authors(authors):
    # First 3 lines convert string to list. list_auth is the final list of authors
    string_auth = authors[1:len(authors) - 1]
    string_auth = string_auth.strip()
    string_auth = string_auth.replace('\'', '')
    list_auth = string_auth.split(",")
    return list_auth


def get_val(authors):
    if type(authors) == str:
        list_auth = get_list_authors(authors)
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


#df['updated_authors'] = df.apply(lambda x: get_val(x['author']), axis=1)
df = df[~df.author.str.contains('Cst Editorial Board', na=False)]
df = df[~df.updated_authors.str.contains('Letters To The Editor', na=False)]

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
    directory = os.path.join("../MIS-COV19/", "dataset/")
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


def update_index_for_all_files():
    files = ['news-dataset_abc_news.csv', "news-dataset_business_insider.csv", "news-dataset_cbs_news.csv",
             "news-dataset_chicago_suntimes.csv", "news-dataset_CNBC.csv", "news-dataset_fiveThirtyEight.csv",
             "news-dataset_npr.csv", "news-dataset_pbs.csv"]
    for fileName in files:
        update_indexes("../dataset/" + fileName)


def remove_values(authors, values):
    if type(authors) == str:
        list_authors = get_list_authors(authors)
        list_authors = [x.strip() for x in list_authors]
        res = [i.strip() for i in list_authors if i not in values]
        return res
    return authors


def remove_specific_values(values):
    df_csv = pd.read_csv("../dataset/news-dataset_chicago_suntimes.csv", index_col=False)
    df_csv['updated_authors'] = df_csv.apply(lambda x: remove_values(x['updated_authors'], values), axis=1)
    df_csv.to_csv("../dataset/news-dataset_chicago_suntimes.csv", index=False)
    update_indexes("../dataset/news-dataset_chicago_suntimes.csv")


remove_specific_values(['Usa Today', 'Better Government Association', 'Usa Today Network', 'Sun-Times Staff Report'])
