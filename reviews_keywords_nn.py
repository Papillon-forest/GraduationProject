import json
import pickle
from pprint import pprint

import nltk as nltk
from nltk import word_tokenize

# import reviews
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

read = json.load(open('datasets/Reviews_Subway Surfers_all.json', 'r', encoding="utf-8"))
rating_reviews_list5 = []
rating_reviews_list4 = []
rating_reviews_list3 = []
rating_reviews_list2 = []
rating_reviews_list1 = []


def classify_reviews_keywords_jj(read):
    for i in range(len(read)):
        sentences = read[i]['text']
        words = word_tokenize(sentences)
        word_list = nltk.pos_tag(words)
        for j in range(len(word_list)):
            if word_list[j][1] == 'NN' or word_list[j][1] == 'NNS':
                # print(word_list[j][0])
                if read[i]['rating'] == 5:
                    rating_reviews_list5.append(word_list[j][0])
                elif read[i]['rating'] == 4:
                    rating_reviews_list4.append(word_list[j][0])
                elif read[i]['rating'] == 3:
                    rating_reviews_list3.append(word_list[j][0])
                elif read[i]['rating'] == 2:
                    rating_reviews_list2.append(word_list[j][0])
                elif read[i]['rating'] == 1:
                    rating_reviews_list1.append(word_list[j][0])
            else:
                continue


# def classify_reviews_keywords_all(n):
#     for i in range(n):
#         classify_reviews_keywords(reviews.get_reviews(i))

def get_reviews_keywords_jj():
    classify_reviews_keywords_jj(read)
    rating_reviews_list5.sort()
    rating_reviews_list4.sort()
    rating_reviews_list3.sort()
    rating_reviews_list2.sort()
    rating_reviews_list1.sort()

    rating_reviews_dict = {'5': rating_reviews_list5,
                           '4': rating_reviews_list4,
                           '3': rating_reviews_list3,
                           '2': rating_reviews_list2,
                           '1': rating_reviews_list1}
    return rating_reviews_dict


def write_reviews_keywords():
    filename = "datasets/Reviews_Subway Surfers_all_keywords_nn.json"
    data = json.dumps(get_reviews_keywords_jj(), indent=1, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data)


def get_reviews_keywords_jj_distinct():
    # count_set = set(lists)
    # count_list = list()
    # for item in count_set:
    #     count_list.append((item, lists.count(item))

    test_set5 = set(rating_reviews_list5)
    rating_reviews_list5_distinct = list()
    for item in test_set5:
        rating_reviews_dict5_distinct = {'keywords': item, 'counts': rating_reviews_list5.count(item)}
        rating_reviews_list5_distinct.append(rating_reviews_dict5_distinct)

    test_set4 = set(rating_reviews_list4)
    rating_reviews_list4_distinct = list()
    for item in test_set4:
        rating_reviews_dict4_distinct = {'keywords': item, 'counts': rating_reviews_list4.count(item)}
        rating_reviews_list4_distinct.append(rating_reviews_dict4_distinct)

    test_set3 = set(rating_reviews_list3)
    rating_reviews_list3_distinct = list()
    for item in test_set3:
        rating_reviews_dict3_distinct = {'keywords': item, 'counts': rating_reviews_list3_distinct.count(item)}
        rating_reviews_list3_distinct.append(rating_reviews_dict3_distinct)

    test_set2 = set(rating_reviews_list2)
    rating_reviews_list2_distinct = list()
    for item in test_set2:
        rating_reviews_dict2_distinct = {'keywords': item, 'counts': rating_reviews_list2.count(item)}
        rating_reviews_list2_distinct.append(rating_reviews_dict2_distinct)

    test_set1 = set(rating_reviews_list1)
    rating_reviews_list1_distinct = list()
    for item in test_set1:
        rating_reviews_dict1_distinct = {'keywords': item, 'counts': rating_reviews_list1.count(item)}
        rating_reviews_list1_distinct.append(rating_reviews_dict1_distinct)

    rating_reviews_list5_distinct = sorted(rating_reviews_list5_distinct, key=lambda x: x['counts'], reverse=True)
    rating_reviews_list4_distinct = sorted(rating_reviews_list4_distinct, key=lambda x: x['counts'], reverse=True)
    rating_reviews_list3_distinct = sorted(rating_reviews_list3_distinct, key=lambda x: x['counts'], reverse=True)
    rating_reviews_list2_distinct = sorted(rating_reviews_list2_distinct, key=lambda x: x['counts'], reverse=True)
    rating_reviews_list1_distinct = sorted(rating_reviews_list1_distinct, key=lambda x: x['counts'], reverse=True)

    rating_reviews_dict_distinct = {'5': rating_reviews_list5_distinct,
                                    '4': rating_reviews_list4_distinct,
                                    '3': rating_reviews_list3_distinct,
                                    '2': rating_reviews_list2_distinct,
                                    '1': rating_reviews_list1_distinct}
    return rating_reviews_dict_distinct


def write_reviews_keywords_jj_distinct():
    filename = "datasets/Reviews_Subway Surfers_distinct_keywords_nn.json"
    data = json.dumps(get_reviews_keywords_jj_distinct(), indent=1, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data)


write_reviews_keywords()
write_reviews_keywords_jj_distinct()
