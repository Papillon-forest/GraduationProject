import json
import datetime
from pprint import pprint

import requests


# /v1.3/apps/{market}/app/{product_id}/reviews?start_date={start_date}&end_date={end_date}&countries={countries}&page_index={page_index}&page_size={page_size}&version={version}&rating={rating}
# "https://api.data.ai/v1.3/apps/ios/app/660004961/reviews?start_date=2018-06-15&end_date=2018-08-15&page_size=3"

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


def get_reviews():
    payload = find_reviews()
    # product_id_temp = input("请输入product_id：")
    # market_temp = input("请输入market：")
    query = f"https://api.data.ai/v1.3/apps/ios/app/1437783446/reviews"
    api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
    headers = {"Authorization": "Bearer " + api_key}
    r = requests.get(query, params=payload, headers=headers)
    # print(r.text)
    output = json.loads(r.text)
    # print(output['reviews'])
    try:
        for i in range(len(output['reviews'])):
            if output['reviews'][i]['country'] != 'US':
                del output['reviews'][i]
            else:
                continue
    except IndexError:
        print("实际数量不足100")
    data = json.dumps(output, indent=1)
    with open("Reviews_Lily's Garden.json", 'w', newline='\n') as f:
        f.write(data)


get_reviews()
