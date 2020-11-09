#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

# Array的创建方法

# 定义一维数组
a = np.array([1, 2, 3], dtype=np.int32)
print(a.dtype)
# int32

b = np.array([1, 2, 3], dtype=np.int64)
print(b.dtype)
# int64

c = np.array([1, 2, 3])
print(c)
# [1 2 3]

d = np.array([[1, 2, 3], [4, 5, 6]])
print(d)
# [[1 2 3]
#  [4 5 6]]

# 生成两行三列全为0的矩阵
zero = np.zeros((2, 3))
print(zero)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 生成三行四列全为1的矩阵
one = np.ones((3, 4))
print(one)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 生成3行2列全都接近于0但不是0的数
empty = np.empty((3, 2))
print(empty)
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

# 生成从0到10不包含10的一维数组
e = np.arange(10)
print(e)
# [0 1 2 3 4 5 6 7 8 9]

# 生成从4到10不包含10的一维数组
f = np.arange(4, 10)
print(f)
# [4 5 6 7 8 9]

# 生成从1到20不包含20,间隔为3的一维数组
g = np.arange(1, 20, 3)
print(g)
# [ 1  4  7 10 13 16 19]

# 重新定义矩阵形状
h = np.arange(8).reshape(2, 4)
print(h)
# [[0 1 2 3]
#  [4 5 6 7]]
