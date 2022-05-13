import csv
from pprint import pprint

import pandas as pd

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


write_retention("datasets/Tetris/2021_Tetris_retention.csv")
# clean_reviews("datasets/Reviews_Subway Surfers_all.json")
# clean_reviews("datasets/Reviews_Plants vs. Zombies_all.json")
# clean_reviews("datasets/Reviews_Angry Birds_all.json")
# clean_reviews("datasets/Reviews_Candy Crush Saga_all.json")
# clean_reviews("datasets/Reviews_Lily's Garden_all.json")
clean_reviews("datasets/Tetris/Reviews_Tetris_all.json")