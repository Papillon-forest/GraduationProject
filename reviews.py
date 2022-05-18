import csv
import json
import datetime
from pprint import pprint
import jieba.analyse
import requests
import paddlehub as hub
import time

# /v1.3/apps/{market}/app/{product_id}/reviews?start_date={start_date}&end_date={end_date}&countries={countries}&page_index={page_index}&page_size={page_size}&version={version}&rating={rating}
# "https://api.data.ai/v1.3/apps/ios/app/660004961/reviews?start_date=2018-06-15&end_date=2018-08-15&page_size=3"
from textblob import TextBlob

# read = json.load(open('Reviews_Subway Surfers_all.json', 'r', encoding="utf-8"))
from main import read_json

senta = hub.Module(name='senta_bilstm')


def find_reviews(start_date='2020-01-01',
                 end_date='2021-12-31',
                 version='all',
                 country='US',
                 rating='all',
                 page_index='0',
                 page_size='100'):
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'version': version,
        'country': country,
        'rating': rating,
        'page_index': page_index,
        'page_size': page_size
    }
    return payload


def get_reviews(page_index_temp):
    time.sleep(6)
    payload = find_reviews(page_index=page_index_temp)
    # product_id_temp = input("请输入product_id：")
    # market_temp = input("请输入market：")
    query = f"https://api.data.ai/v1.3/apps/ios/app/1491074310/reviews"
    api_key = 'b8d45ab5aa36a5dd757e07d70eb796a5bca9e9c4'
    headers = {"Authorization": "Bearer " + api_key}
    r = requests.get(query, params=payload, headers=headers)
    # print(r.text)
    output = json.loads(r.text)
    # pprint(output)
    print(f"第{page_index_temp + 1}页：")
    print("总共的Reviews数量为：")
    print(len(output['reviews']))
    del_list = []
    try:
        for i in range(len(output['reviews'])):
            if output['reviews'][i]['country'] == "US":
                continue
            else:
                del_list.append(i)
    except IndexError:
        print("实际长度不足100")
    # print(output['reviews'][99])
    print("不符合要求的Reviews数量为：")
    print(len(del_list))
    print("符合要求的Reviews数量为：")
    print(len(output['reviews']) - len(del_list))
    # print("\n")
    for i in reversed(del_list):
        # print(i)
        # print(len(output['reviews']))
        del output['reviews'][i]
    for i in range(len(output['reviews'])):
        reviews_list = [output['reviews'][i]['text']]
        # senta = hub.Module(name='senta_bilstm')
        test_text = reviews_list
        results = senta.sentiment_classify(texts=test_text, use_gpu=False, batch_size=1)
        del results[0]['text']
        output['reviews'][i]['sentiment'] = results[0]
        keywords = jieba.analyse.extract_tags(output['reviews'][i]['text'], topK=3, withWeight=False)
        output['reviews'][i]['keywords'] = keywords
        print(f"第{page_index_temp + 1}页,第{i + 1}条评论分析完成")
    print(f"第{page_index_temp + 1}页装载完成")

    return output


def get_reviews_all(start_n, end_n):
    reviews_list_all = []
    for i in range(start_n, end_n):
        reviews_list_all.extend(get_reviews(i)['reviews'])
    return reviews_list_all


def write_reviews():
    output = get_reviews(146)
    data = json.dumps(output, indent=1, ensure_ascii=False)
    with open("datasets/Sample/Reviews_Tetris.json", 'w', newline='\n') as f:
        f.write(data)
        print("样本成功写入文件")


def write_reviews_all(start_n, end_n):
    data = json.dumps(get_reviews_all(start_n, end_n), indent=1, ensure_ascii=False)
    with open("datasets/Tetris/Reviews_Tetris_all.json", 'a', newline='\n') as f:
        f.write(data)
        print(f"第{start_n + 1}页到第{end_n}页评论成功写入文件")


def get_reviews_sentiment(file):
    read = read_json(f"datasets/{file}/Reviews_{file}_all.json")
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


def write_reviews_sentiment(file):
    date_list_all = get_reviews_sentiment(file)
    data = json.dumps(date_list_all, indent=1, ensure_ascii=False)
    with open(f"datasets/{file}/Reviews_{file}_all_sentiment_percent.json", 'w', newline='\n') as f:
        f.write(data)


def get_reviews_rating(file):
    read = read_json(f"datasets/{file}/Reviews_{file}_all.json")
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
            'rating_5_percent': (counts_5) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_4_percent': (counts_4) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_3_percent': (counts_3) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_2_percent': (counts_2) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_1_percent': (counts_1) / (counts_5 + counts_4 + counts_3 + counts_2 + counts_1),
            'rating_average': (counts_5 * 5 + counts_4 * 4 + counts_3 * 3 + counts_2 * 2 + counts_1) / (
                    counts_5 + counts_4 + counts_3 + counts_2 + counts_1)
        }
        date_rating_list_all.append(date_dict)
        date_rating_list_all = sorted(date_rating_list_all, key=lambda x: x['keywords'], reverse=False)
    return date_rating_list_all


def write_reviews_rating(file):
    date_rating_list_all = get_reviews_rating(file)
    data = json.dumps(date_rating_list_all, indent=1, ensure_ascii=False)
    with open(f"datasets/{file}/Reviews_{file}_all_rating_percent_average.json", 'w', newline='\n') as f:
        f.write(data)


# write_reviews()
# for i in range(10, 140, 10):
#     write_reviews_all(i, i + 10)
#     time.sleep(120)
#
# write_reviews_all(140, 146)
write_reviews_sentiment("Angry Birds")
write_reviews_sentiment("Candy Crush Saga")
write_reviews_sentiment("Plants vs. Zombies")
write_reviews_sentiment("Subway Surfers")
write_reviews_sentiment("Lily's Garden")
write_reviews_sentiment("Tetris")