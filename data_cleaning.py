import csv
import json
from pprint import pprint

import pandas as pd
from textblob import TextBlob

from main import read_csv, read_json


def clean_retention(file):
    datas = []
    read = read_csv(file)
    for row in read:
        datas.append(row)
    for data_front in datas[:10]:
        datas.remove(data_front)
    for data_back in datas[-4:]:
        datas.remove(data_back)
    return datas


def write_retention(file):
    datas_list = clean_retention(file)
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datas_list)


def clean_reviews(file):
    reviews_ids = []
    read = read_json(file)
    print(len(read))
    for i in range(len(read)):
        if read[i]['review_id'] not in reviews_ids:
            reviews_ids.append(read[i]['review_id'])
    if len(read) != len(reviews_ids):
        print("有重合！")
    else:
        print("无重合")


def clean_sentiment(file):
    read = read_json(file)
    for i in range(len(read)):
        text = read[i]['text']
        blob = TextBlob(text)
        if blob.sentiment[0] < -0.1:
            read[i]['sentiment']['sentiment_key'] = 'negative'
        elif blob.sentiment[0] > 0.1:
            read[i]['sentiment']['sentiment_key'] = 'positive'
        elif -0.1 < blob.sentiment[0] < 0.1 and blob.sentiment[1] == 0:
            read[i]['sentiment']['sentiment_key'] = 'neutral'
        read[i]['sentiment']['subjective'] = blob.sentiment[1]
        # del read[i]['sentiment']['sentiment_label']
        # del read[i]['sentiment']['positive_probs']
        # del read[i]['sentiment']['negative_probs']
    data = json.dumps(read, indent=1, ensure_ascii=False)
    with open(file, 'w', newline='\n') as f:
        f.write(data)


clean_sentiment('datasets/Angry Birds/Reviews_Angry Birds_all.json')
clean_sentiment('datasets/Candy Crush Saga/Reviews_Candy Crush Saga_all.json')
clean_sentiment('datasets/Plants vs. Zombies/Reviews_Plants vs. Zombies_all.json')
clean_sentiment('datasets/Subway Surfers/Reviews_Subway Surfers_all.json')
clean_sentiment("datasets/Lily's Garden/Reviews_Lily's Garden_all.json")
clean_sentiment("datasets/Tetris/Reviews_Tetris_all.json")

# write_retention("datasets/Woodoku/2020_Woodoku_retention.csv")
# write_retention("datasets/Fishdom/2020_Fishdom_retention.csv")
# write_retention("datasets/Wordscapes/2020_Wordscapes_retention.csv")
# write_retention("datasets/Among us/2020_Among us_retention.csv")
# write_retention("datasets/Project Makeover/2020_Project Makeover_retention.csv")
# write_retention("datasets/Woodoku/2021_Woodoku_retention.csv")
# write_retention("datasets/Fishdom/2021_Fishdom_retention.csv")
# write_retention("datasets/Wordscapes/2021_Wordscapes_retention.csv")
# write_retention("datasets/Among us/2021_Among us_retention.csv")
# write_retention("datasets/Project Makeover/2021_Project Makeover_retention.csv")
# write_retention("datasets/Homescapes/2020_Homescapes_retention.csv")
# write_retention("datasets/Homescapes/2021_Homescapes_retention.csv")
# clean_reviews("datasets/Reviews_Subway Surfers_all.json")
# clean_reviews("datasets/Reviews_Plants vs. Zombies_all.json")
# clean_reviews("datasets/Reviews_Angry Birds_all.json")
# clean_reviews("datasets/Reviews_Candy Crush Saga_all.json")
# clean_reviews("datasets/Reviews_Lily's Garden_all.json")
# clean_reviews("datasets/Tetris/Reviews_Tetris_all.json")
