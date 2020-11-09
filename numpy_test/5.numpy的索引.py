#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.arange(2, 14)
print(arr1)
# [ 2  3  4  5  6  7  8  9 10 11 12 13]


# 第二个位置的数据
print(arr1[2])
# 4


# 第一到第四个位置的数据
print(arr1[1:4])
# [3 4 5]


# 从第二个位置到倒数第一个位置的数据
print(arr1[2:-1])
# [ 4  5  6  7  8  9 10 11 12]


# 前5个数据
print(arr1[:5])
# [2 3 4 5 6]


# 后两个数据
print(arr1[-2:])
# [12 13]


arr2 = arr1.reshape(3, 4)
print(arr2)
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]


# 第二行数据
print(arr2[1])
# [6 7 8 9]


# 第二行第二列元素
print(arr2[1][1])
print(arr2[1, 1])
# 7
# 7

# 所有行的第二列
print(arr2[:, 2])
# [ 4  8 12]


# 迭代行
for i in arr2:
    print(i)
# [2 3 4 5]
# [6 7 8 9]
# [10 11 12 13]


# 迭代列
for i in arr2.T:
    print(i)
# [ 2  6 10]
# [ 3  7 11]
# [ 4  8 12]
# [ 5  9 13]

# 一个一个元素迭代
for i in arr2.flat:
    print(i)
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
