import pandas as pd
import os
import re

reliable_dir = '../dataset/reliable'
unreliable_dir = '../dataset/unreliable'

CSV_FILE_DIR_HEAD = "../"
CSV_FILE_DIR_RELIABLE = CSV_FILE_DIR_HEAD + "dataset/reliable"
CSV_FILE_DIR_UNRELIABLE = CSV_FILE_DIR_HEAD + "dataset/unreliable_new"

files = ['news-dataset_abc_news.csv', "news-dataset_business_insider.csv", "news-dataset_cbs_news.csv",
         "news-dataset_chicago_suntimes.csv", "news-dataset_CNBC.csv", "news-dataset_fiveThirtyEight.csv",
         "news-dataset_npr.csv", "news-dataset_pbs.csv", "news-dataset-reuters.csv", "news-dataset-slate.csv",
         "news-dataset_atlantic.csv",
         "news-dataset_mercury_news.csv", "news-dataset_new_yorker.csv", "news-dataset_the_verge.csv",
         "news-dataset_washington_post_old.csv", 'news-dataset_usa_today.csv', 'news-dataset_washington_monthly.csv',
         'news-dataset_yahoo_news.csv', 'news-dataset_nytimes_uncleaned.csv']

url_filter_patterns = "opinion|live-updates|pictures|video|archive|la-voz|cn.reuters|jp.reuters|lta.reuters|'it.businessinsider.com/"

# df = pd.read_csv(reliable_dir + '/news-dataset_chicago_suntimes.csv", index_col=False)
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


#
#
# #df['updated_authors'] = df.apply(lambda x: get_val(x['author']), axis=1)
# #df = df[~df.author.str.contains('Cst Editorial Board', na=False)]
# #df = df[~df.updated_authors.str.contains('Letters To The Editor', na=False)]
#
# #df.to_csv(reliable_dir + '/news-dataset_chicago_suntimes.csv", index=False)
#
#
def update_indexes(fileName):
    df_fileName = pd.read_csv(fileName)
    df_fileName.set_index('url')
    df_fileName = df_fileName.drop('news_id', axis=1)
    df_fileName.index.name = 'news_id'
    fileName1 = fileName.rsplit("/")[3]
    print(fileName1)
    df_fileName.to_csv(fileName)


#
# # Do not run this function
# def read_files_from_directory():
#     directory = os.path.join("../MIS-COV19/", "dataset/")
#     print(directory)
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             print(file)
#             file = directory + file
#             if file.endswith(".csv") and file.find("_old") == -1:
#                 f = open(file, 'r')
#                 update_indexes(file)
#                 #  perform calculation
#                 f.close()
#
#
# def update_index_for_all_files():
#     files = ['news-dataset_abc_news.csv', "news-dataset_business_insider.csv", "news-dataset_cbs_news.csv",
#              "news-dataset_chicago_suntimes.csv", "news-dataset_CNBC.csv", "news-dataset_fiveThirtyEight.csv",
#              "news-dataset_npr.csv", "news-dataset_pbs.csv"]
#     for fileName in files:
#         update_indexes(reliable_dir + '/' + fileName)
#
#
# def remove_values(authors, values):
#     if type(authors) == str:
#         list_authors = get_list_authors(authors)
#         print(list_authors)
#         list_authors = [x.strip() for x in list_authors]
#         res = [i.strip() for i in list_authors if i not in values]
#         return res
#     return authors
#
#
# def remove_specific_values(values):
#     df_csv = pd.read_csv(reliable_dir + "/news-dataset_chicago_suntimes.csv", index_col=False)
#     #df_csv['updated_authors'] = df_csv.apply(lambda x: remove_values(x['updated_authors'], values), axis=1)
#     df_csv.to_csv(reliable_dir + "/news-dataset_chicago_suntimes.csv", index=False)
#     update_indexes(reliable_dir + "/news-dataset_chicago_suntimes.csv")
#
#
# #remove_specific_values(['Usa Today', 'Better Government Association', 'Usa Today Network', 'Sun-Times Staff Report'])
#
#  For pbs remove news id =1
# df_pbs = pd.read_csv(reliable_dir + "/news-dataset_pbs.csv", index_col=False)
# df_pbs = df_pbs[df['news_id'] != 1]
# df_pbs.to_csv(reliable_dir + "/news-dataset_pbs.csv", index=False)
# update_indexes(reliable_dir + "/news-dataset_pbs.csv")
# update_indexes(reliable_dir + "/news-dataset_los_angeles_daily.csv")

def drop_author():
    df_sun = pd.read_csv(reliable_dir + "/news-dataset_chicago_suntimes.csv", index_col=False)
    df_sun = df_sun.drop(['author'], axis=1)
    df_sun.rename(columns={'updated_authors': 'author'}, inplace=True)


# Re-order Columns
def reorder_cols():
    df_sun = pd.read_csv(reliable_dir + "/news-dataset_chicago_suntimes.csv", index_col=False)
    df_sun1 = df_sun[['url', 'publisher', 'publish_date', 'author', 'title', 'image', 'body_text']]
    df_sun1.index.name = 'news_id'
    df_sun1 = df_sun1.drop_duplicates(subset="image", keep=False)
    # df_sun1.to_csv(reliable_dir + "/news-dataset_chicago_suntimes.csv")
    print(df_sun1['title'])


def drop_duplicates():
    for fileName in files:
        df_fileName = pd.read_csv(reliable_dir + "/" + fileName)
        # print(len(df_fileName.title.unique()))
        print(fileName, len(df_fileName))
        df_fileName.drop_duplicates(subset='title', inplace=True)
        print("After")
        print(fileName, len(df_fileName))
        df_fileName.to_csv(reliable_dir + "/" + fileName, index=False)
        update_indexes(reliable_dir + "/" + fileName)


# drop_duplicates()


def remove_row(fileName, id):
    df_remove_row = pd.read_csv(fileName)
    df_remove_row = df_remove_row[df_remove_row['news_id'] != id]
    df_remove_row.to_csv(fileName, index=False)
    update_indexes(fileName)


# remove_row(reliable_dir + '/news-dataset_business_insider.csv', 112)
# remove_row(reliable_dir + '/news-dataset-reuters.csv', 42)
# remove_row(reliable_dir + '/news-dataset-slate.csv', 13)
# remove_row(reliable_dir + '/news-dataset_usa_today.csv', 120)
# remove_row(reliable_dir + '/news-dataset_usa_today.csv', 18)
# remove_row(reliable_dir + '/news-dataset_yahoo_news.csv', 15)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 0)

# remove rows with empty body
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 1)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 3)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 6)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 18)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 35)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 40)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 66)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 69)
# remove_row(reliable_dir + '/news-dataset_nytimes.csv', 73)
# remove_row(unreliable_dir + '/news-dataset_drudgereport.csv', 3)
# remove_row(unreliable_dir + '/news-dataset_big_league_politics.csv', 7)
# remove_row(unreliable_dir + '/news-dataset_big_league_politics.csv', 8)
#remove_row(unreliable_dir + '/news-dataset_drudgereport.csv', 20)

def stripe_spaces(authors):
    authors = get_list_authors(authors)
    new_authors = []
    for value in authors:
        j = value.strip()
        j = j.replace('"', '')
        new_authors.append(j)
    print(new_authors)
    return new_authors


remove_from_authors = ['May', 'Apr', 'April', 'Mar', 'March', 'Contributors', 'Published P.M. Et', 'Usa Today',
                       'Associated Press',
                       'West Coast Correspondent', 'Senior Writer',
                       'Senior Political Correspondent', 'Yahoo News Staff', 'Senior Editor', 'National Correspondent',
                       'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                       'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                       'Sexy-Author-Bio', 'Background', 'Ffffff', 'Border-Style', 'Solid', 'Border-Color', 'Color',
                       'Border-Top-Width', 'Border-Right-Width',
                       'Cristina Began Writing For The Gateway Pundit In', 'She Is Currently The Associate Editor.',
                       'Jim Hoft Is The Founder Of The Gateway Pundit',
                       'One Of The Top Conservative News Outlets In America. Jim Was Awarded The Reed Irvine Accuracy In Media Award In',
                       'Is The Proud Recipient Of The Breitbart Award For Excellence In Online Journalism The Americans For Prosperity Foundation In May'
                       'At P.M.', 'Min Read', 'Https', 'Abc News', 'Www.Axios.Com Authors Caitlin']
reuters_authors = ['Min Read', 'Reuters Editorial']


def remove_redundant_information(authors, remove_authors_list):
    authors = stripe_spaces(authors)
    for author in remove_authors_list:
        if author.strip() in authors:
            authors.remove(author)
    return authors


def update_authors(fileName, remove_authors):
    df_update_authors = pd.read_csv(fileName)
    print(df_update_authors['author'])

    df_update_authors['author'] = df_update_authors.apply(
        lambda x: remove_redundant_information(x['author'], remove_authors), axis=1)
    df_update_authors.to_csv(fileName, index=False)

    print(df_update_authors['author'])


# update_authors(reliable_dir + "/news-dataset_the_verge.csv", remove_from_authors)
# update_authors(reliable_dir + "/news-dataset-reuters.csv", reuters_authors)
# update_authors(reliable_dir + "/news-dataset_usa_today.csv", remove_from_authors)
# update_authors(reliable_dir + "/news-dataset_yahoo_news.csv", remove_from_authors)
# update_authors(unreliable_dir + "/news-dataset_natural_news.csv", remove_from_authors)
# update_authors(unreliable_dir + "/news-dataset_gateway_pundit.csv", remove_from_authors)
# update_authors(unreliable_dir + "/news-dataset_drudgereport.csv", remove_from_authors)


def update_authors_spaces(fileName):
    df_update_authors = pd.read_csv(fileName)
    print(df_update_authors['author'])
    df_update_authors['author'] = df_update_authors.apply(lambda x: stripe_spaces(x['author']), axis=1)
    df_update_authors.to_csv(reliable_dir + "/news-dataset_the_verge.csv", index=False)


# update_authors_spaces(reliable_dir + "/news-dataset_the_verge.csv")

def replace_text(text, value, by_value):
    return text.replace(value, by_value)


def replace_values_body_text(fileName, value_to_replace, by_value):
    replace_body_df = pd.read_csv(fileName)
    replace_body_df['body_text'] = replace_body_df.apply(
        lambda x: replace_text(x['body_text'], value_to_replace, by_value), axis=1)
    print(replace_body_df['body_text'])
    replace_body_df.to_csv(reliable_dir + "/news-dataset_washington_post.csv", index=False)


# replace_values_body_text(reliable_dir + "/news-dataset_washington_post_old.csv", 'AD', '')

# update_indexes(reliable_dir + "/news-dataset_pbs.csv")
# update_indexes(reliable_dir + "/news-dataset_los_angeles_daily.csv")
# update_indexes(reliable_dir + "/news-dataset_yahoo_news.csv")
# update_indexes(reliable_dir + "/news-dataset_nytimes.csv")
# update_indexes(unreliable_dir + "/news-dataset_gateway_pundit.csv")
# update_indexes(reliable_dir + "/news-dataset-politico.csv")
# update_indexes(unreliable_dir + "/news-dataset_infowars.csv")
# update_indexes(unreliable_dir + "/news-dataset_rt_news.csv")
# update_indexes(unreliable_dir + "/news-dataset_activistpost.csv")
# update_indexes(unreliable_dir + "/news-dataset_american_thinker.csv")
# update_indexes(unreliable_dir + "/news-dataset_bipartisan_report.csv")
# update_indexes(unreliable_dir + "/news-dataset_clashdaily.csv")
# update_indexes(unreliable_dir + "/news-dataset_collective_evolution.csv")
# update_indexes(unreliable_dir + "/news-dataset_dirty_laundry.csv")
# update_indexes(unreliable_dir + "/news-dataset_infowars.csv")
# update_indexes(unreliable_dir + "/news-dataset_news_punch.csv")
# update_indexes(unreliable_dir + "/news-dataset_RealFarmacy.csv")
# update_indexes(unreliable_dir + "/news-dataset_theduran.csv")

def get_valid_url(url):
    return re.search(url_filter_patterns, url) is None


def filter_url(fileName):
    df_filter_url = pd.read_csv(fileName)
    df_filter_url['url_valid'] = df_filter_url.apply(lambda x: get_valid_url(x['url']), axis=1)
    df_filter_url = df_filter_url[df_filter_url['url_valid'] == True]
    df_filter_url = df_filter_url.drop('url_valid', axis=1)
    df_filter_url.to_csv(reliable_dir + "/news-dataset_nytimes.csv", index=False)


# filter_url(reliable_dir + "/news-dataset_nytimes.csv")

def update_reuters():
    df12 = pd.read_csv("../dataset/reliable/news-dataset-reuters.csv")
    df12 = df12.drop('Unnamed: 0', axis=1)
    df12.reset_index(drop=True, inplace=True)
    df12.to_csv("../dataset/reliable/news-dataset-reuters.csv")
    print(df12)


def update_index_all(directory):
    CSV_FILE_NAMES = os.listdir(directory)

    for CSV_FILE_NAME in CSV_FILE_NAMES:
        if CSV_FILE_NAME[:12] == "news-dataset":
            fileName = directory + '/' + CSV_FILE_NAME
            update_indexes(fileName)
            #print(fileName)



update_index_all(CSV_FILE_DIR_UNRELIABLE)

# sputnik_df = pd.read_csv(unreliable_dir + "/news-dataset_sputnik_news.csv")
# def get_date_From_url(url):
#     url_parts = url.split('/')
#     date1 = url_parts[4][:8]
#     format_date = '-'.join([date1[:4], date1[4:6], date1[6:]])
#     return format_date
#
# sputnik_df['publish_date'] = sputnik_df.apply(lambda x: get_date_From_url(x['url']), axis=1)
# sputnik_df.to_csv(unreliable_dir + "/news-dataset_sputnik_news.csv", index=False)

