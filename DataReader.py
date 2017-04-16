import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datas = pd.read_csv("C:\Data\dm\data\data_csv.csv")
# datas.dropna(inplace=True)

value_index_list = [3, 4, 5, 6, 16, 19, 20, 22, 25, 26, 27]

for i in range(1, 29):
    print "Feature #" + str(i) + ": "

    if value_index_list.__contains__(i):
        # temp = datas[str(i)].value_counts()
        # most_number = temp.keys()[0]

        max = datas[str(i)].max()
        min = datas[str(i)].min()
        mean = datas[str(i)].mean()
        med = datas[str(i)].median()
        na = 300 - datas[str(i)].dropna().size

        # datas[str(i)].fillna(most_number, inplace=True)

        index = pd.Series([max, min, mean, med, na], ["max", "min", "mean", "median", "nan"])

        # img = datas[str(i)].plot(kind='bar')
        img = datas[str(i)].plot(kind='box')
        plt.savefig("C:\Data\dm\img\\" + str(i) + ".png")
        plt.close()

    else:
        index = datas[str(i)].value_counts()

    print index



