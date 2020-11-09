#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 垂直合并
arr3 = np.vstack((arr1, arr2))
print(arr3)
print(arr3.shape)
# [[1 2 3]
#  [4 5 6]]
# (2, 3)

# 水平合并
arr4 = np.hstack((arr1, arr2))
print(arr4)
print(arr4.shape)
# [1 2 3 4 5 6]
# (6,)


arr = np.concatenate((arr1, arr2, arr1))
print(arr)
# [1 2 3 4 5 6 1 2 3]


# 垂直合并, 合并array的维度要相同，形状要匹配
arrv = np.concatenate((arr1, arr1), axis=0)
print(arrv)
# [1 2 3 1 2 3]


# 纵向合并，合并array的维度要相同，形状要匹配, 不能是一维数据
arrh = np.concatenate((arr3, arr3), axis=1)
print(arrh)
# [[1 2 3 1 2 3]
#  [4 5 6 4 5 6]]


print(arr1.T)
# [1 2 3]

arr1_1 = arr1[np.newaxis, :]
print(arr1_1)
# [[1 2 3]]

print(arr1_1.T)
# [[1]
#  [2]
#  [3]]


arr1_2 = arr1[:, np.newaxis]
print(arr1_2)
print(arr1_2.T)
# [[1]
#  [2]
#  [3]]
# [[1 2 3]]

# 将数据转换成二维数据
arr1_3 = np.atleast_2d(arr1)
print(arr1_3)

# [[1 2 3]]
