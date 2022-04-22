import json
import datetime
from pprint import pprint
import jieba.analyse
import requests

# /v1.3/apps/{market}/app/{product_id}/reviews?start_date={start_date}&end_date={end_date}&countries={countries}&page_index={page_index}&page_size={page_size}&version={version}&rating={rating}
# "https://api.data.ai/v1.3/apps/ios/app/660004961/reviews?start_date=2018-06-15&end_date=2018-08-15&page_size=3"
from textblob import TextBlob


def find_reviews(start_date='2022-01-01',
                 end_date=datetime.date.today(),
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
    payload = find_reviews(page_index=page_index_temp)
    # product_id_temp = input("请输入product_id：")
    # market_temp = input("请输入market：")
    query = f"https://api.data.ai/v1.3/apps/ios/app/512939461/reviews"
    api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
    headers = {"Authorization": "Bearer " + api_key}
    r = requests.get(query, params=payload, headers=headers)
    # print(r.text)
    output = json.loads(r.text)
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
        blob = TextBlob(output['reviews'][i]['text'])
        output['reviews'][i]['polarity'] = blob.sentiment[0]
        output['reviews'][i]['subjectivity'] = blob.sentiment[1]
        keywords = jieba.analyse.extract_tags(output['reviews'][i]['text'], topK=3, withWeight=False)
        output['reviews'][i]['keywords'] = keywords
    return output


def get_reviews_all(n):
    reviews_list = []
    for i in range(n):
        reviews_list.extend(get_reviews(i)['reviews'])
    return reviews_list


def write_reviews():
    output = get_reviews(0)
    data = json.dumps(output, indent=1, ensure_ascii=False)
    with open("Reviews_Subway Surfers.json", 'w', newline='\n') as f:
        f.write(data)


def write_reviews_all(n):
    data = json.dumps(get_reviews_all(n), indent=1, ensure_ascii=False)
    with open("Reviews_Subway Surfers_all.json", 'w', newline='\n') as f:
        f.write(data)



