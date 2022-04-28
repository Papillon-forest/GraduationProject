import csv
import datetime
import time
from pprint import pprint

dates = []
dates_1 = []
dates_2 = []
dates_3 = []
dates_4 = []
dates_5 = []
dates_6 = []
dates_7 = []
dates_8 = []
dates_9 = []
dates_10 = []
dates_11 = []
dates_12 = []
def get_retention():
    filename = 'datasets/data-ai_Intelligence_Single_table_report_2021-01-01_2022-01-31.csv'
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            dates.append(row)

    del_list = []
    # pprint(len(dates))
    dela = datetime.timedelta(days=1)
    for i in range(len(dates)):
        date = datetime.datetime.strptime(dates[i][1], "%Y-%m-%d")
        dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * float(dates[i][0])
        if date.year == 2022:
            del_list.append(i)
        elif date.month == 1:
            dates_1.append(dates[i])
        elif date.month == 2:
            dates_2.append(dates[i])
        elif date.month == 3:
            dates_3.append(dates[i])
        elif date.month == 4:
            dates_4.append(dates[i])
        elif date.month == 5:
            dates_5.append(dates[i])
        elif date.month == 6:
            dates_6.append(dates[i])
        elif date.month == 7:
            dates_7.append(dates[i])
        elif date.month == 8:
            dates_8.append(dates[i])
        elif date.month == 9:
            dates_9.append(dates[i])
        elif date.month == 10:
            dates_10.append(dates[i])
        elif date.month == 11:
            dates_11.append(dates[i])
        elif date.month == 12:
            dates_12.append(dates[i])
    for i in reversed(del_list):
        del dates[i]
    dates_dict = {
        '1': dates_1,
        '2': dates_2,
        '3': dates_3,
        '4': dates_4,
        '5': dates_5,
        '6': dates_6,
        '7': dates_7,
        '8': dates_8,
        '9': dates_9,
        '10': dates_10,
        '11': dates_11,
        '12': dates_12,
    }
    return dates_dict


# pprint(dates_1)
def write_retention():
    filename = 'datasets/Retention_Subway Surfers.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Retention Days', 'Start Date', 'End Date', 'User Retention'])
        writer.writerows(dates_1)
        writer.writerows(dates_2)
        writer.writerows(dates_3)
        writer.writerows(dates_4)
        writer.writerows(dates_5)
        writer.writerows(dates_6)
        writer.writerows(dates_7)
        writer.writerows(dates_8)
        writer.writerows(dates_9)
        writer.writerows(dates_10)
        writer.writerows(dates_11)
        writer.writerows(dates_12)

# get_retention()
# write_retention()