import json
from pprint import pprint

import jieba.analyse
import nltk
import requests
from nltk import word_tokenize

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

text = "Dear professors,I feel so glad to meet all of you here.My name is Xia Yi, 21 years old,and I come from " \
       "Jiangsu. I am a senior student majoring in computer Science and Technology in Beijing Forestry University.I am " \
       "a sunny and positive boy. I strive for excellence in study, and I enjoy socializing in life. As a college " \
       "student,I am well aware that the new era is a competition between IQ and EQ. College life makes me gradually " \
       "clearly identify myself,I think of myself as a pragmatist 	pursuing high efficiency, I insist 'or is not " \
       "done,or is done best' principle of doing things, 	and that's what makes me paranoid about some knowledge " \
       "points sometimes, but I also think 	it maybe a good thing.All work and no play makes Jack a dull boy. In my " \
       "spare time, I prefer to play basketball and read some history-related books, civilizing my spirit and my " \
       "body. These hobbies finally won me the school-level Scholarship.I have been interested in computers and " \
       "geography since CHILDHOOD. When I was in middle school, I could name all the neighbors of any given country " \
       "on the world map. At the same time, I still have great interest in computer. These are the reasons why I " \
       "apply for this major.If I am admitted,I would be very delighted and honored.The above is my " \
       "self-introduction,thank you. "
# blob = TextBlob(text)
# print(blob.sentiment)
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
pprint(keywords[0])
