#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(array)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 维度
print(array.ndim)
# 2

# 形状
print(array.shape)
# (3, 3)

# 大小
print(array.size)
# 9

# 元素属性
print(array.dtype)
# int64
