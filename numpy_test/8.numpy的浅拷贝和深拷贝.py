#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.array([1, 2, 3])

# 共享一块内存
arr2 = arr1
arr2[0] = 5

print(arr1)
print(arr2)
# [5 2 3]
# [5 2 3]

# 深拷贝
arr3 = arr1.copy()
arr3[0] = 6
print(arr1)
print(arr3)
# [5 2 3]
# [6 2 3]
