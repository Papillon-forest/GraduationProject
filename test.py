import datetime
import json
import ssl
import time
from pprint import pprint

import jieba.posseg
import nltk
import requests
import wordcloud as wordcloud
from matplotlib import pyplot as plt
from nltk import word_tokenize
# import paddlehub as hub
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
#
# def read_json(json_str):
#     read_temp = json.load(open(json_str, 'r', encoding="utf-8"))
#     return read_temp
#
#
# read = read_json('Reviews_Subway Surfers_all.json')
#
# date_dict = {
#     'keywords': '',
#     'counts': 0,
#     'positive_percent': 0
# }
#
# date_list_all = []
# date_list = []
# for i in range(len(read)):
#     date_list.append(read[i]['date'])
# test_date_list = set(date_list)
# date_list_distinct = list()
# for item in test_date_list:
#     count = 0
#     for i in range(len(read)):
#         if item == read[i]['date'] and read[i]['sentiment']['sentiment_key'] == 'positive':
#             count = count + 1
#     date_dict = {'keywords': item, 'counts': date_list.count(item), 'positive_percent': count / date_list.count(item)}
#     date_list_all.append(date_dict)

# print('1')
# time.sleep(10)
# print('2')
# time.sleep(10)
# print('3')
# print(datetime.date.today())
# print (ssl.OPENSSL_VERSION)
# text='Ta chido'
# result=jieba.posseg.lcut(text)
# print(result)
# from matplotlib.font_manager import FontManager
#
# mpl_fonts = set(f.name for f in FontManager().ttflist)
#
# print('all font list get from matplotlib.font_manager:')
# for f in sorted(mpl_fonts):
#     print('\t' + f)
# text = '***-I love China'
# text=text.replace('*', '')
# text=text.replace('@', '')
# text=text.replace('#', '')
# text=text.replace('%', '')
# text=text.replace('^', '')
# text=text.replace('&', '')
# pprint(text)
def read_json(json_str):
    read_temp = json.load(open(json_str, 'r', encoding="utf-8"))
    return read_temp


read = read_json('Reviews_Subway Surfers_distinct_keywords_nn.json')
dict_temp = {}
# key = read['5'][0]['keywords']
# pprint(key)
# dict_temp[key] = read['5'][0]['counts']
# pprint(dict_temp)
for i in range(len(read['5'])):
    key = read['5'][i]['keywords']
    dict_temp[key] = read['5'][i]['counts']
wordcloud = wordcloud.WordCloud(background_color='White').fit_words(dict_temp)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
