import pandas as pd
from csv import reader


def unique():
    list1 = ['MSISDN']
    with open('sample_csv.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row[0] not in list1:
                print(row[0] + ' ' + row[2] + ' ' + row[3])
                list1.append(row[0])


unique()
