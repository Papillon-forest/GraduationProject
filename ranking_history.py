import datetime
import json

import requests


def find_ranking_history(
        start_date='2022-01-01',
        end_date=datetime.date.today(),
        interval='daily',
        countries='US',
        category='Overall',
        feed='free',
        device='iphone'
):
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'interval': interval,
        'countries': countries,
        'category': category,
        'feed': feed,
        'device': device
    }
    return payload


def get_ranking_history():
    payload = find_ranking_history()
    product_id_temp = input("请输入product_id：")
    # market_temp = input("请输入market：")
    query = f"https://api.data.ai/v1.3/apps/ios/app/{product_id_temp}/ranks"
    api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
    headers = {"Authorization": "Bearer " + api_key}
    r = requests.get(query, params=payload, headers=headers)
    output = json.loads(r.text)
    return output
