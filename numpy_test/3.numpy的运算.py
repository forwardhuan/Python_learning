#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
# [[1 2 3]
#  [4 5 6]]

arr2 = np.array([[1, 1, 2], [2, 3, 3]])
print(arr2)
# [[1 1 2]
#  [2 3 3]]

# 加法，按位加
print(arr1 + arr2)
# [[2 3 5]
#  [6 8 9]]

# 减法， 按位减
print(arr1 - arr2)
# [[0 1 1]
#  [2 2 3]]

# 乘法， 按位乘
print(arr1 * arr2)
# [[ 1  2  6]
#  [ 8 15 18]]

# 幂运算， 按位
print(arr1 ** arr2)
# [[  1   2   9]
#  [ 16 125 216]]

# 除法， 按位相除
print(arr1 / arr2)
# [[1.         2.         1.5       ]
#  [2.         1.66666667 2.        ]]

# 取余
print(arr1 % arr2)
# [[0 0 1]
#  [0 2 0]]

# 取整
print(arr1 // arr2)
# [[1 2 1]
#  [2 1 2]]

# 矩阵每一个元素加2
print(arr1 + 2)
# [[3 4 5]
#  [6 7 8]]

# 矩阵所有元素乘10
print(arr1 * 10)
# [[10 20 30]
#  [40 50 60]]

# 判读矩阵中每个元素是否大于3
print(arr1 > 3)
# [[False False False]
#  [ True  True  True]]

arr3 = np.ones((3, 5))
print(arr3)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# 矩阵的乘法
print(np.dot(arr1, arr3))
# [[ 6.  6.  6.  6.  6.]
#  [15. 15. 15. 15. 15.]]

print(arr1.dot(arr3))
# [[ 6.  6.  6.  6.  6.]
#  [15. 15. 15. 15. 15.]]

# 矩阵转置
print(arr1)
# [[1 2 3]
#  [4 5 6]]
print(arr1.T)
# [[1 4]
#  [2 5]
#  [3 6]]
print(np.transpose(arr1))
# [[1 4]
#  [2 5]
#  [3 6]]
