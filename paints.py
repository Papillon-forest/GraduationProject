import datetime
import json
import time
from pprint import pprint
import matplotlib.pyplot as plt


def read_json(json_str):
    read = json.load(open(json_str, 'r', encoding="utf-8"))
    return read


def get_reviews_sentiment():
    read = read_json('Reviews_Subway Surfers_all.json')
    date_dict = {
        'keywords': '',
        'counts': 0,
        'positive_percent': 0
    }
    date_list_all = []
    date_list = []
    for i in range(len(read)):
        date_list.append(read[i]['date'])
    test_date_list = set(date_list)
    date_list_distinct = list()
    for item in test_date_list:
        count = 0
        for i in range(len(read)):
            if item == read[i]['date'] and read[i]['sentiment']['sentiment_key'] == 'positive':
                count = count + 1
        date_dict = {'keywords': item, 'counts': date_list.count(item),
                     'positive_percent': count / date_list.count(item)}
        date_list_all.append(date_dict)
        date_list_all = sorted(date_list_all, key=lambda x: x['keywords'], reverse=False)
    return date_list_all


def write_reviews_sentiment():
    date_list_all = get_reviews_sentiment()
    data = json.dumps(date_list_all, indent=1, ensure_ascii=False)
    with open("Reviews_Subway Surfers_all_sentiment_percent.json", 'w', newline='\n') as f:
        f.write(data)


def paint_sentiment_line():
    date_list_all = get_reviews_sentiment()
    sample = []
    for i in range(len(date_list_all)):
        sample.append(date_list_all[i]['positive_percent'])
    x = []
    y = []
    for i in range(len(date_list_all)):
        x.append(date_list_all[i]['keywords'])
    y.extend(sample)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=3)
    plt.show()

paint_sentiment_line()
