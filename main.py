import csv
import json
import datetime

# import ranking_history
# import reviews
from pprint import pprint


def read_json(json_str):
    read = json.load(open(json_str, 'r', encoding="utf-8"))
    return read


def read_csv(csv_str):
    read = csv.reader(open(csv_str, 'r', encoding='utf-8'))
    return read
# Subway Surfers:512939461
