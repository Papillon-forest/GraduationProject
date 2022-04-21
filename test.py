import json
from pprint import pprint

import nltk
import requests
from nltk import word_tokenize

# query ='https://api.data.ai/v1.3/apps/ios/app/1403455040/ratings'
# api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
# headers = {"Authorization": "Bearer " + api_key}
# r = requests.get(query,headers=headers)
# output = json.loads(r.text)
# pprint(output)

sentences = "It's my pet"
words = word_tokenize(sentences)
word_list = nltk.pos_tag(words)
print(word_list)