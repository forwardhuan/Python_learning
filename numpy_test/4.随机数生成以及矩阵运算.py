#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 生成随机数的方式

import numpy as np

# 生成3行2列从0到1的随机数
sample = np.random.random((3, 2))
print(sample)
# [[0.94800964 0.91867228]
#  [0.3680591  0.14434706]
#  [0.33398542 0.50719141]]

# 生成3行2列符合标准正态分布的随机数
sample2 = np.random.normal(size=(3, 2))
print(sample2)
# [[ 0.22708609 -0.79131841]
#  [ 0.66393757 -0.18234665]
#  [ 0.98113021  0.93463262]]


# 生成3行2列从0到10的随机整数
sample3 = np.random.randint(0, 10, size=(3, 2))
print(sample3)
# [[4 7]
#  [5 9]
#  [6 2]]


# 矩阵求和
print(np.sum(sample3))
# 33


# 矩阵求最小值
print(np.min(sample3))
# 2

# 矩阵求最大值
print(np.max(sample3))
# 9

# 矩阵列求和
print(np.sum(sample3, axis=0))
# [15 18]

# 矩阵行求和
print(np.sum(sample3, axis=1))
# [11 14  8]


# 矩阵最小值的索引
print(np.argmin(sample3))
print(sample3.argmin())
# 5
# 5


# 矩阵最大值的索引
print(np.argmax(sample3))
print(sample3.argmax())
# 3
# 3


# 矩阵所有元素的平均值
print(np.mean(sample3))
print(sample3.mean())
# 5.5
# 5.5


# 求所有元素的中位数
print(np.median(sample3))
# 5.5


# 求所有元素开方
print(np.sqrt(sample3))
# [[2.         2.64575131]
#  [2.23606798 3.        ]
#  [2.44948974 1.41421356]]


sample4 = np.random.randint(0, 10, size=(1, 10))
print(sample4)
# [[7 4 1 1 7 6 3 3 7 2]]


# 随机数排序
print(np.sort(sample4))
# [[1 1 2 3 3 4 6 7 7 7]]


# 矩阵每一行排序
print(np.sort(sample))
# [[0.91867228 0.94800964]
#  [0.14434706 0.3680591 ]
#  [0.33398542 0.50719141]]


# 小于2的变成2，大于7的变成7， 控制数字范围
print(np.clip(sample4, 2, 7))
# [[7 4 2 2 7 6 3 3 7 2]]
