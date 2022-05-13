import csv
import datetime
import json
import ssl
import time
from pprint import pprint

import jieba.posseg
import nltk
import numpy as np
import requests
import scipy
import wordcloud as wordcloud
from matplotlib import pyplot as plt
from nltk import word_tokenize
# import paddlehub as hub
# query ='https://api.data.ai/v1.3/intelligence/apps/ios/ranking?countries=US&categories=Overall&feeds=grossing&ranks=3&granularity=daily&device=iphone&start_date=2018-04-07 '
# api_key = 'f62c2fcc2e9e14defa7f8e3e9dc0bb99c25bcfcb'
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
from scipy.optimize import curve_fit, fsolve, root

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
# def read_json(json_str):
#     read_temp = json.load(open(json_str, 'r', encoding="utf-8"))
#     return read_temp
#
#
# read = read_json('Reviews_Subway Surfers_distinct_keywords_nn.json')
# dict_temp = {}
# # key = read['5'][0]['keywords']
# # pprint(key)
# # dict_temp[key] = read['5'][0]['counts']
# # pprint(dict_temp)
# for i in range(len(read['5'])):
#     key = read['5'][i]['keywords']
#     dict_temp[key] = read['5'][i]['counts']
# wordcloud = wordcloud.WordCloud(background_color='White').fit_words(dict_temp)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

# filename = 'datasets/2021_Subway Surfers_retention.csv'
# with open(filename,'r') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     dates = []
#     for row in reader:
#         dates.append(row)
#
# del_list = []
# # pprint(len(dates))
#
# for i in range(len(dates)):
#     date = datetime.datetime.strptime(dates[i][1], "%Y-%m-%d")
#     if date.year == 2022:
#         del_list.append(i)
# for i in reversed(del_list):
#     del dates[i]
#
# # pprint(dates)
#
# filename = 'datasets/All_Subway Surfers_retention.csv'
# with open(filename,'w') as f:
#     writer=csv.writer(f)
#     writer.writerow(['Retention Days','Start Date','End Date','User Retention'])
#     writer.writerows(dates)
# date='2021-01-01'
# d='2'
# date_temp=datetime.datetime.strptime(date, "%Y-%m-%d")
# dela=datetime.timedelta(days=1)
# data_new= datetime.date(date_temp.year, date_temp.month, date_temp.day)+dela*float(d)
# # print(data_new)
# str='100.00%'
# str=str.replace('%','')
# print(float(str))

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model, datasets

#
# from paints import read_csv
#
# read = read_csv('datasets/All_Subway Surfers_retention.csv')
# header_now = next(read)
# x = []
# y = []
# x_date = [1, 2, 3, 4, 5, 6, 7, 8, 15, 31]
# y_rate = []
# # print(x_date)
# for row in read:
#     y_temp = float(row[3].replace('%', '')) / 100
#
#     y.append(y_temp)
#
# for y in y[:10]:
#     y_rate.append(y)
# pprint(y_rate)
# x_train = np.array(x_date)
# y_train = np.array(y_rate)
#
# pprint(x_train)
#
#
# def func_power(x, a, b):
#     return x ** a + b
#
#
# popt, pcov = curve_fit(func_power, x_date, y_rate)
# pprint(popt)
# x1 = range(1, 32)
# y1 = [func_power(i, popt[0], popt[1]) for i in x1]
# plt.scatter(x_date, y_rate, color="Blue")
# plt.scatter(x1, y1, color='Red')
# plt.show()

# def func(i):
#     a, b = i[0], i[1]
#     return [
#         x_date[0] ** a + b - y_rate[0],
#         x_date[1] ** a + b - y_rate[1],
#         x_date[2] ** a + b - y_rate[2],
#         x_date[3] ** a + b - y_rate[3],
#         x_date[4] ** a + b - y_rate[4],
#         x_date[5] ** a + b - y_rate[5],
#         x_date[6] ** a + b - y_rate[6],
#         x_date[7] ** a + b - y_rate[7],
#         x_date[8] ** a + b - y_rate[8],
#         x_date[9] ** a + b - y_rate[9]
#     ]
#
#
# result = root(func, np.array([0, 0]), method='lm')
# print(result.x)
# housing_data=datasets.load_boston()
# pprint(housing_data.data[0])

# for i in range(0,140,10):
#     print(i,i+10)

# f = open("datasets/Reviews_Subway Surfers_all.json", "r", encoding='utf-8')
# str = f.read()
# pprint(str)
# str.replace('1', ',')
# pprint(str)
x=[1,2,3,4,5,6,7,8]
x=np.array(x).reshape(-1,1)
pprint(x)
pprint(x[:,0])