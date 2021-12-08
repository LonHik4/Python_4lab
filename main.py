# -*- coding: cp1251 -*-
import pandas as pd
from multiprocessing import Pool
from time import time
from matplotlib import pyplot as plt
import numpy as np


def calculate(*data):
    a=list(data)
    return sum(a)


df = pd.read_csv("data.csv", sep=",", encoding='windows-1251')
print(df["�������� ������"].tolist())
calculate()

if __name__=="__main__":
    time_1 = time()
    lst=[]
    for i in range(1, 5):
        with Pool(i) as p:
            print(p.apply(calculate, df["�������� ������"].tolist()))
        a=time() - time_1
        lst.append(a)
        print(time() - time_1)
    print(lst)

    fig=plt.figure(figsize=(10, 10))
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('y=sinc(x)')
    plt.scatter(list(range(1,5)),lst, color='teal', marker='o', linewidths=2, facecolors='none')
    plt.show()