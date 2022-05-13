import csv
import datetime
import json
import time
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import wordcloud as wc

# import json
#
# # 由于文件中有多行，直接读取会出现错误，因此一行一行读取
# file = open("papers.json", 'r', encoding='utf-8')
# papers = []
# for line in file.readlines():
#     dic = json.loads(line)
#     papers.append(dic)
#
# print(len(papers))
from sklearn import preprocessing

from main import read_json, read_csv
from retentions import get_retention
from reviews import get_reviews_rating, get_reviews_sentiment

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))


def paint_sentiment_line():
    date_list_all = get_reviews_sentiment()

    x = []
    y = []
    for i in range(len(date_list_all)):
        date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            x.append(date_list_all[i]['keywords'])
    for i in range(len(date_list_all)):
        date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            y.append(date_list_all[i]['positive_percent'])

    pprint(x)
    pprint(y)
    y = data_scaler.fit_transform(np.array(y).reshape(-1, 1))
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.set_title("User Sentiment Change Map", color='Blue', fontsize=24)
    ax.set_xlabel("Date", color='Blue', fontsize=14)
    ax.set_ylabel("The degree of positive", color='Blue', fontsize=14)
    ax.plot(x, y, linewidth=3)
    ax.scatter(x, y, color='Red')
    plt.show()


def paint_rating_line():
    date_rating_list_all = get_reviews_rating()

    x = []
    y = []
    for i in range(len(date_rating_list_all)):
        date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            x.append(date_rating_list_all[i]['keywords'])
    for i in range(len(date_rating_list_all)):
        date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            y.append(date_rating_list_all[i]['rating_average'])

    pprint(x)
    pprint(y)
    y = data_scaler.fit_transform(np.array(y).reshape(-1, 1))
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.set_title("User Rating Change Map", color='Blue', fontsize=24)
    ax.set_xlabel("Date", color='Blue', fontsize=14)
    ax.set_ylabel("Rating average", color='Blue', fontsize=14)
    ax.plot(x, y, linewidth=3)
    ax.scatter(x, y, color='Red')
    plt.show()


def paint_all():
    date_list_all = get_reviews_sentiment()

    x1 = []
    y1 = []
    for i in range(len(date_list_all)):
        date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            x1.append(date_list_all[i]['keywords'])
    for i in range(len(date_list_all)):
        date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            y1.append(date_list_all[i]['positive_percent'])

    pprint(x1)
    pprint(y1)

    # plt.style.use('seaborn')
    # fig, ax = plt.subplots()
    # fig.autofmt_xdate()
    # ax.set_title("User Sentiment Change Map", color='Blue', fontsize=24)
    # ax.set_xlabel("Date", color='Blue', fontsize=14)
    # ax.set_ylabel("The degree of positive", color='Blue', fontsize=14)
    # ax.plot(x1, y1, linewidth=3)
    # ax.scatter(x1, y1, color='Red')

    date_rating_list_all = get_reviews_rating()

    x2 = []
    y2_average = []
    y2_5 = []
    y2_4 = []
    y2_3 = []
    y2_2 = []
    y2_1 = []
    for i in range(len(date_rating_list_all)):
        date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            x2.append(date_rating_list_all[i]['keywords'])
    for i in range(len(date_rating_list_all)):
        date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        if date.year == 2021 and date.month == 0o1:
            y2_average.append(date_rating_list_all[i]['rating_average'])
            y2_5.append(date_rating_list_all[i]['rating_5_percent'])
            y2_4.append(date_rating_list_all[i]['rating_4_percent'])
            y2_3.append(date_rating_list_all[i]['rating_3_percent'])
            y2_2.append(date_rating_list_all[i]['rating_2_percent'])
            y2_1.append(date_rating_list_all[i]['rating_1_percent'])

    # pprint(x2)
    # pprint(y2)

    read = read_csv('datasets/All_Subway Surfers_retention.csv')
    header_now = next(read)
    x3 = []
    y3 = []
    x3_date = []
    y3_rate = []
    for row in read:
        x3_temp = row[0]
        y3_temp = float(row[3].replace('%', '')) / 100
        x3.append(x3_temp)
        y3.append(y3_temp)

    # x3_date.append(0)
    # y3_rate.append(1)
    for x3 in x3[:9]:
        x3_date.append(x3)
    for y3 in y3[:9]:
        y3_rate.append(y3)

    y1 = data_scaler.fit_transform(np.array(y1).reshape(-1, 1))
    y2_average = data_scaler.fit_transform(np.array(y2_average).reshape(-1, 1))
    y2_5 = data_scaler.fit_transform(np.array(y2_5).reshape(-1, 1))
    y2_4 = data_scaler.fit_transform(np.array(y2_4).reshape(-1, 1))
    y2_3 = data_scaler.fit_transform(np.array(y2_3).reshape(-1, 1))
    y2_2 = data_scaler.fit_transform(np.array(y2_2).reshape(-1, 1))
    y2_1 = data_scaler.fit_transform(np.array(y2_1).reshape(-1, 1))

    plt.style.use('seaborn')
    # fig, ax = plt.subplots()
    fig = plt.figure()
    plt.title("Changes in user reviews and ratings related to retention", fontsize=24)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Degree", fontsize=14)
    fig.autofmt_xdate()
    plt.plot(x1, y1, label='Sentiment', color='Red', linewidth=3, linestyle='-', marker='o')
    plt.plot(x2, y2_average, label='Rating_Ave', color='Blue', linewidth=3, linestyle='-', marker='^')
    plt.plot(x2, y2_5, label='Rating_5', color='Blue', linewidth=1, linestyle='-', marker='^')
    # plt.plot(x2, y2_4, label='Rating_4', color='Blue', linewidth=3, linestyle='-', marker='^')
    # plt.plot(x2, y2_3, label='Rating_3', color='Blue', linewidth=3, linestyle='-', marker='^')
    # plt.plot(x2, y2_2, label='Rating_2', color='Blue', linewidth=3, linestyle='-', marker='^')
    # plt.plot(x2, y2_1, label='Rating_1', color='Blue', linewidth=3, linestyle='-', marker='^')
    plt.plot(x3_date, y3_rate, label='Retention', color='Green', linewidth=3, linestyle='-', marker='s')
    plt.legend()  # 让图例生效
    plt.show()


def paint_keywords_nn_wordcloud():
    read = read_json('datasets/Reviews_Subway Surfers_distinct_keywords_nn.json')
    dict_temp = {}
    # key = read['5'][0]['keywords']
    # pprint(key)
    # dict_temp[key] = read['5'][0]['counts']
    # pprint(dict_temp)
    for i in range(len(read['5'])):
        key = read['5'][i]['keywords']
        dict_temp[key] = read['5'][i]['counts']
    wordcloud = wc.WordCloud(background_color='White').fit_words(dict_temp)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def paint_keywords_jj_wordcloud():
    read = read_json('datasets/Reviews_Subway Surfers_distinct_keywords_jj.json')
    dict_temp = {}
    # key = read['5'][0]['keywords']
    # pprint(key)
    # dict_temp[key] = read['5'][0]['counts']
    # pprint(dict_temp)
    for i in range(len(read['5'])):
        key = read['5'][i]['keywords']
        dict_temp[key] = read['5'][i]['counts']
    wordcloud = wc.WordCloud(background_color='White').fit_words(dict_temp)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def paint_user_retention():
    read = read_csv('datasets/All_Subway Surfers_retention.csv')
    header_now = next(read)
    x = []
    y = []
    x_date = []
    y_rate = []
    for row in read:
        x_temp = row[0]
        y_temp = float(row[3].replace('%', '')) / 100
        x.append(x_temp)
        y.append(y_temp)
    for x in x[:10]:
        x_date.append(x)
    for y in y[:10]:
        y_rate.append(y)
    # pprint(y_rate)
    #
    #
    # pprint(y_rate)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.set_title("User Retention Change Map", color='Blue', fontsize=24)
    ax.set_xlabel("Date", color='Blue', fontsize=14)
    ax.set_ylabel("The degree of retention", color='Blue', fontsize=14)
    ax.scatter(x_date, y_rate, color='Red')
    plt.show()


paint_all()
