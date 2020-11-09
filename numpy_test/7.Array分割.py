#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.arange(12).reshape((3, 4))
print(arr1)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]


# 水平方向分成两份，等分
arr2, arr3 = np.split(arr1, 2, axis=1)
print(arr2)
print(arr3)
# [[0 1]
#  [4 5]
#  [8 9]]
# [[ 2  3]
#  [ 6  7]
#  [10 11]]


# 垂直方向分割, 等分
arr4, arr5, arr6 = np.split(arr1, 3, axis=0)
print(arr4)
print(arr5)
print(arr6)
# [[0 1 2 3]]
# [[4 5 6 7]]
# [[ 8  9 10 11]]


# 水平方向分成三份, 不等分
arr7, arr8, arr9 = np.array_split(arr1, 3, axis=1)
print(arr7)
print(arr8)
print(arr9)
# [[0 1]
#  [4 5]
#  [8 9]]
# [[ 2]
#  [ 6]
#  [10]]
# [[ 3]
#  [ 7]
#  [11]]



arrv1, arrv2, arrv3 = np.vsplit(arr1, 3)
print(arrv1)
print(arrv2)
print(arrv3)
# [[0 1 2 3]]
# [[4 5 6 7]]
# [[ 8  9 10 11]]
