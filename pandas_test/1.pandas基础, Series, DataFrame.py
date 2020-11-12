#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

s1 = pd.Series([4, 7, -5, 3])  # 创建一个series，索引为默认值
print(s1)
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64

print(s1.values)  # series的值
# [ 4  7 -5  3]

print(s1.index)  # series的索引
# RangeIndex(start=0, stop=4, step=1)

s2 = pd.Series([4, 0, 6, 5], index=['a', 'b', 'c', 'd'])  # 指定索引
print(s2)
# a    4
# b    0
# c    6
# d    5
# dtype: int64

print(s2['b'])  # 根据索引取值
# 0

print(s2[['a', 'c', 'd']])  # 根据索引取多个值
# a    4
# c    6
# d    5
# dtype: int64

print('b' in s2)
# True

# Series可以看作是一个定长的有序字典
dic1 = {'apple': 5, 'pen': 3, 'applepen': 10}
s3 = pd.Series(dic1)
print(s3)
# apple        5
# pen          3
# applepen    10
# dtype: int64

# DataFrame
data = {'year': [2014, 2015, 2016, 2017],
        'income': [1000, 2000, 3000, 5000],
        'pay': [500, 1000, 2000, 4000]}
df1 = pd.DataFrame(data)
print(df1)
#    year  income   pay
# 0  2014    1000   500
# 1  2015    2000  1000
# 2  2016    3000  2000
# 3  2017    5000  4000

df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df2)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['a', 'b', 'c'], columns=[2, 33, 44, 5])
print(df3)
#    2   33  44  5
# a   0   1   2   3
# b   4   5   6   7
# c   8   9  10  11


print(df1.columns)
# Index(['year', 'income', 'pay'], dtype='object')

print(df1.index)
# RangeIndex(start=0, stop=4, step=1)

print(df1.values)
# [[2014 1000  500]
#  [2015 2000 1000]
#  [2016 3000 2000]
#  [2017 5000 4000]]

print(df1.describe())
#               year       income          pay
# count     4.000000     4.000000     4.000000
# mean   2015.500000  2750.000000  1875.000000
# std       1.290994  1707.825128  1547.847968
# min    2014.000000  1000.000000   500.000000
# 25%    2014.750000  1750.000000   875.000000
# 50%    2015.500000  2500.000000  1500.000000
# 75%    2016.250000  3500.000000  2500.000000
# max    2017.000000  5000.000000  4000.000000

print(df1.T)
#            0     1     2     3
# year    2014  2015  2016  2017
# income  1000  2000  3000  5000
# pay      500  1000  2000  4000

# 列排序
print(df1.sort_index(axis=1))
#    income   pay  year
# 0    1000   500  2014
# 1    2000  1000  2015
# 2    3000  2000  2016
# 3    5000  4000  2017

# 行排序
print(df1.sort_index(axis=0))
#    year  income   pay
# 0  2014    1000   500
# 1  2015    2000  1000
# 2  2016    3000  2000
# 3  2017    5000  4000

print(df1.sort_values(by='pay'))
#    year  income   pay
# 0  2014    1000   500
# 1  2015    2000  1000
# 2  2016    3000  2000
# 3  2017    5000  4000
