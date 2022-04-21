import json
import pickle
from pprint import pprint

import nltk as nltk
from nltk import word_tokenize

import reviews
import jieba.posseg

# CC  并列连词          NNS 名词复数        UH 感叹词
# CD  基数词              NNP 专有名词        VB 动词原型
# DT  限定符            NNP 专有名词复数    VBD 动词过去式
# EX  存在词            PDT 前置限定词      VBG 动名词或现在分词
# FW  外来词            POS 所有格结尾      VBN 动词过去分词
# IN  介词或从属连词     PRP 人称代词        VBP 非第三人称单数的现在时
# JJ  形容词            PRP$ 所有格代词     VBZ 第三人称单数的现在时
# JJR 比较级的形容词     RB  副词            WDT 以wh开头的限定词
# JJS 最高级的形容词     RBR 副词比较级      WP 以wh开头的代词
# LS  列表项标记         RBS 副词最高级      WP$ 以wh开头的所有格代词
# MD  情态动词           RP  小品词          WRB 以wh开头的副词
# NN  名词单数           SYM 符号            TO  to

output = reviews.get_reviews()
print(len(output['reviews']))
rating_reviews_list5 = []
rating_reviews_list4 = []
rating_reviews_list3 = []
rating_reviews_list2 = []
rating_reviews_list1 = []
rating_reviews_dict = {'5': rating_reviews_list5,
                       '4': rating_reviews_list4,
                       '3': rating_reviews_list3,
                       '2': rating_reviews_list2,
                       '1': rating_reviews_list1}
for i in range(len(output['reviews'])):
    sentences = output['reviews'][i]['text']
    words = word_tokenize(sentences)
    word_list = nltk.pos_tag(words)
    for j in range(len(word_list)):
        if word_list[j][1] == 'JJ':
            # print(word_list[j][0])
            if output['reviews'][i]['rating'] == 5:
                rating_reviews_list5.append(word_list[j][0])
            elif output['reviews'][i]['rating'] == 4:
                rating_reviews_list4.append(word_list[j][0])
            elif output['reviews'][i]['rating'] == 3:
                rating_reviews_list3.append(word_list[j][0])
            elif output['reviews'][i]['rating'] == 2:
                rating_reviews_list2.append(word_list[j][0])
            elif output['reviews'][i]['rating'] == 1:
                rating_reviews_list1.append(word_list[j][0])
        else:
            continue
filename = "Reviews_Subway Surfers_keywords_jj.json"
data=json.dumps(rating_reviews_dict,indent=1,ensure_ascii=False)
with open(filename, 'w') as f:
    f.write(data)
