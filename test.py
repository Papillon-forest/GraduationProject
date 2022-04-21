import json
from pprint import pprint

import requests

query ='https://api.data.ai/v1.3/apps/ios/app/1403455040/ranks?start_date=2018-07-22&end_date=2018-08-01&interval' \
       '=daily&countries=US&category=Overall&feed=free'
api_key = '06f7b2a02a5b78c3ec95ba206c71569f55487533'
headers = {"Authorization": "Bearer " + api_key}
r = requests.get(query,headers=headers)
output = json.loads(r.text)
pprint(output)