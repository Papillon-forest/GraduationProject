import datetime
import json
import time
from pprint import pprint

import jieba.analyse
import nltk
import requests
from nltk import word_tokenize
import paddlehub as hub
# query ='https://api.data.ai/v1.3/apps/ios/app/1403455040/ratings'
# api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
# headers = {"Authorization": "Bearer " + api_key}
# r = requests.get(query,headers=headers)
# output = json.loads(r.text)
# pprint(output)

# sentences = "It's my pet"
# words = word_tokenize(sentences)
# word_list = nltk.pos_tag(words)
# print(word_list)

# list_old=['good','good','nice']
# test_set=set(list_old)
# list_distinct=list(test_set)
# pprint(list_distinct)

from textblob import TextBlob


# text = ["I love it"]
# # blob = TextBlob(text)
# # print(blob.sentiment)
# # keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
# # pprint(keywords[0])
#
# senta = hub.Module(name='senta_bilstm')
#
# test_text = text
#
# results = senta.sentiment_classify(texts=test_text, use_gpu=False, batch_size=1)
#
# pprint(results[0])


# temp=datetime.date.today()
# day=datetime.timedelta(days=1)
# print(temp-24*day)
# while d<=end_date:
#     print(d)
#     d+=day

# read = json.load(open('Reviews_Subway Surfers_all.json', 'r', encoding="utf-8"))
# pprint(len(read))

# end_time=datetime.date.today()
# delta=datetime.timedelta(days=1)
# start_time=end_time-7*delta
# print(end_time)
# print(start_time)

def read_json(json_str):
    read_temp = json.load(open(json_str, 'r', encoding="utf-8"))
    return read_temp


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
    date_dict = {'keywords': item, 'counts': date_list.count(item), 'positive_percent': count / date_list.count(item)}
    date_list_all.append(date_dict)

