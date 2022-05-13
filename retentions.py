import csv
import datetime
import time
from pprint import pprint

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit




def get_retention(file):
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
    dates = []
    filename = file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            dates.append(row)

    del_list = []
    pprint(dates)
    dela = datetime.timedelta(days=1)
    date_temp = datetime.datetime.strptime(dates[0][1], "%Y-%m-%d")
    for i in range(len(dates)):
        date = datetime.datetime.strptime(dates[i][1], "%Y-%m-%d")
        if date.year != date_temp.year or dates[i][3] == '100.00%':
            del_list.append(i)
        elif date.month == 1:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_1.append(dates[i])
        elif date.month == 2:
            if dates[i][0] == '30':
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * 26
            else:
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_2.append(dates[i])
        elif date.month == 3:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_3.append(dates[i])
        elif date.month == 4:
            if dates[i][0] == '30':
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * 29
            else:
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_4.append(dates[i])
        elif date.month == 5:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_5.append(dates[i])
        elif date.month == 6:
            if dates[i][0] == '30':
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * 29
            else:
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_6.append(dates[i])
        elif date.month == 7:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_7.append(dates[i])
        elif date.month == 8:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_8.append(dates[i])
        elif date.month == 9:
            if dates[i][0] == '30':
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * 29
            else:
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_9.append(dates[i])
        elif date.month == 10:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_10.append(dates[i])
        elif date.month == 11:
            if dates[i][0] == '30':
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * 29
            else:
                dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
            dates_11.append(dates[i])
        elif date.month == 12:
            dates[i][0] = datetime.date(date.year, date.month, date.day) + dela * (float(dates[i][0]) - 1)
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
def write_retention(file):
    dates_dict=get_retention(file)
    filename = "datasets/Tetris/All_Tetris_retention.csv"
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(dates_dict['1'])
        writer.writerows(dates_dict['2'])
        writer.writerows(dates_dict['3'])
        writer.writerows(dates_dict['4'])
        writer.writerows(dates_dict['5'])
        writer.writerows(dates_dict['6'])
        writer.writerows(dates_dict['7'])
        writer.writerows(dates_dict['8'])
        writer.writerows(dates_dict['9'])
        writer.writerows(dates_dict['10'])
        writer.writerows(dates_dict['11'])
        writer.writerows(dates_dict['12'])


# def write_retention_new():
#     filename = 'datasets/All_Subway Surfers_retention.csv'
#     with open(filename, 'r') as f:
#         read = csv.reader(f)
#         header_row = next(read)
#         x = []
#         y = []
#         x_date = [1, 2, 3, 4, 5, 6, 7, 8, 15, 31]
#         y_rate = []
#         # print(x_date)
#         for row in read:
#             y_temp = float(row[3].replace('%', '')) / 100
#
#             y.append(y_temp)
#
#         for y in y[:10]:
#             y_rate.append(y)
#         pprint(y_rate)
#         x_train = np.array(x_date)
#         y_train = np.array(y_rate)
#
#         pprint(x_train)
#
#         def func_power(x, a, b):
#             return x ** a + b
#
#         popt, pcov = curve_fit(func_power, x_date, y_rate)
#         pprint(popt)
#         x1 = [9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#         y1 = [func_power(i, popt[0], popt[1]) for i in x1]
#         plt.scatter(x_date, y_rate, color="Blue")
#         plt.scatter(x1, y1, color='Red')
#         plt.show()


write_retention("datasets/Tetris/2020_Tetris_retention.csv")
write_retention("datasets/Tetris/2021_Tetris_retention.csv")
