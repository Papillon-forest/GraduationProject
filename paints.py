import datetime
import json
import time
from pprint import pprint
import matplotlib.pyplot as plt
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
def read_json(json_str):
    read = json.load(open(json_str, 'r', encoding="utf-8"))
    return read


def get_reviews_sentiment():
    read = read_json('Reviews_Subway Surfers_all.json')
    date_senti_dict = {
        'keywords': '',
        'counts': 0,
        'positive_percent': 0
    }
    date_senti_list_all = []
    date_senti_list = []
    for i in range(len(read)):
        date_senti_list.append(read[i]['date'])
    test_date_senti_list = set(date_senti_list)
    date_senti_list_distinct = list()
    for item in test_date_senti_list:
        count = 0
        for i in range(len(read)):
            if item == read[i]['date'] and read[i]['sentiment']['sentiment_key'] == 'positive':
                count = count + 1
        date_dict = {'keywords': item, 'counts': date_senti_list.count(item),
                     'positive_percent': count / date_senti_list.count(item)}
        date_senti_list_all.append(date_dict)
        date_senti_list_all = sorted(date_senti_list_all, key=lambda x: x['keywords'], reverse=False)
    return date_senti_list_all


def write_reviews_sentiment():
    date_list_all = get_reviews_sentiment()
    data = json.dumps(date_list_all, indent=1, ensure_ascii=False)
    with open("Reviews_Subway Surfers_all_sentiment_percent.json", 'w', newline='\n') as f:
        f.write(data)


def paint_sentiment_line():
    date_list_all = get_reviews_sentiment()

    x = []
    y = []
    for i in range(len(date_list_all)):
        # date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        x.append(date_list_all[i]['keywords'])
    for i in range(len(date_list_all)):
        # date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        y.append(date_list_all[i]['positive_percent'])

    pprint(x)
    pprint(y)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.set_title("User Sentiment Change Map", color='Blue', fontsize=24)
    ax.set_xlabel("Date", color='Blue', fontsize=14)
    ax.set_ylabel("The degree of positive", color='Blue', fontsize=14)
    ax.plot(x, y, linewidth=3)
    ax.scatter(x, y, color='Red')
    plt.show()


def get_reviews_rating():
    read = read_json('Reviews_Subway Surfers_all.json')
    date_rating_dict = {
        'keywords': '',
        'counts_5': 0,
        'counts_4': 0,
        'counts_3': 0,
        'counts_2': 0,
        'counts_1': 0,
        'rating_percent': 0
    }
    date_rating_list_all = []
    date_rating_list = []
    for i in range(len(read)):
        date_rating_list.append(read[i]['date'])
    test_date_rating_list = set(date_rating_list)
    date_rating_list_distinct = list()
    for item in test_date_rating_list:
        counts_5 = 0
        counts_4 = 0
        counts_3 = 0
        counts_2 = 0
        counts_1 = 0
        for i in range(len(read)):
            if item == read[i]['date']:
                if read[i]['rating'] == 5:
                    counts_5 = counts_5 + 1
                elif read[i]['rating'] == 4:
                    counts_4 = counts_4 + 1
                elif read[i]['rating'] == 3:
                    counts_3 = counts_3 + 1
                elif read[i]['rating'] == 2:
                    counts_2 = counts_2 + 1
                elif read[i]['rating'] == 1:
                    counts_1 = counts_1 + 1
        date_dict = {
            'keywords': item,
            'counts_5': counts_5,
            'counts_4': counts_4,
            'counts_3': counts_3,
            'counts_2': counts_2,
            'counts_1': counts_1,
            'rating_percent': (counts_5) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_average': (counts_5 * 5 + counts_4 * 4 + counts_3 * 3 + counts_2 * 2 + counts_1) / (
                    counts_5 + counts_4 + counts_3 + counts_2 + counts_1)
        }
        date_rating_list_all.append(date_dict)
        date_rating_list_all = sorted(date_rating_list_all, key=lambda x: x['keywords'], reverse=False)
    return date_rating_list_all


def write_reviews_rating():
    date_rating_list_all = get_reviews_rating()
    data = json.dumps(date_rating_list_all, indent=1, ensure_ascii=False)
    with open("Reviews_Subway Surfers_all_rating_percent_average.json", 'w', newline='\n') as f:
        f.write(data)


def paint_rating_line():
    date_rating_list_all = get_reviews_rating()

    x = []
    y = []
    for i in range(len(date_rating_list_all)):
        # date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        x.append(date_rating_list_all[i]['keywords'])
    for i in range(len(date_rating_list_all)):
        # date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        y.append(date_rating_list_all[i]['rating_average'])

    pprint(x)
    pprint(y)

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
        # date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2021 and date.month == 0o4:
        x1.append(date_list_all[i]['keywords'])
    for i in range(len(date_list_all)):
        # date = datetime.datetime.strptime(date_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2021 and date.month == 0o4:
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
    y2 = []
    for i in range(len(date_rating_list_all)):
        # date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        x2.append(date_rating_list_all[i]['keywords'])
    for i in range(len(date_rating_list_all)):
        # date = datetime.datetime.strptime(date_rating_list_all[i]['keywords'], "%Y-%m-%d")
        # if date.year == 2022 and date.month == 0o4:
        y2.append(date_rating_list_all[i]['rating_percent'])

    pprint(x2)
    pprint(y2)

    plt.style.use('seaborn')
    # fig, ax = plt.subplots()
    fig = plt.figure()
    plt.title("User Sentiment and Rating Change Map", fontsize=24)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Degree", fontsize=14)
    fig.autofmt_xdate()
    plt.plot(x1, y1, label='Senti', color='Red', linewidth=3, linestyle='-', marker='o')
    plt.plot(x2, y2, label='Rating', color='Blue', linewidth=3, linestyle='-', marker='^')
    plt.legend()  # 让图例生效
    plt.show()


def paint_keywords_nn_wordcloud():
    read = read_json('Reviews_Subway Surfers_distinct_keywords_nn.json')
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
    read = read_json('Reviews_Subway Surfers_distinct_keywords_jj.json')
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


paint_keywords_jj_wordcloud()
