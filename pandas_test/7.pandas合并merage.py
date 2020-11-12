#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
# 2  K2  A2  B2
# 3  K3  A3  B3
print(right)
#   key   C   D
# 0  K0  C0  D0
# 1  K1  C1  D1
# 2  K2  C2  D2
# 3  K3  C3  D3

res = pd.merge(left, right, on='key')
print(res)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# how=[’left', 'right', 'inner', 'outer']
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')  # how 默认inner
print(res)
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K1   K1   A1   B1  NaN  NaN
# 2   K2   K0   A2   B2   C2   D2
# 3   K3   K1   A3   B3  NaN  NaN
# 4   K1   K0  NaN  NaN   C1   D1
# 5   K3   K0  NaN  NaN   C3   D3

# 合并两个都有的
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # how 默认inner
print(res)
#   key1 key2   A   B   C   D
# 0   K0   K0  A0  B0  C0  D0
# 1   K2   K0  A2  B2  C2  D2

res = pd.merge(left, right, on=['key1', 'key2'], how='left')  # how 默认inner
print(res)
#   key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K1   K1  A1  B1  NaN  NaN
# 2   K2   K0  A2  B2   C2   D2
# 3   K3   K1  A3  B3  NaN  NaN

res = pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator='indication_column')  # how 默认inner
print(res)
#   key1 key2    A    B    C    D      indication_column
# 0   K0   K0   A0   B0   C0   D0        both
# 1   K1   K1   A1   B1  NaN  NaN   left_only
# 2   K2   K0   A2   B2   C2   D2        both
# 3   K3   K1   A3   B3  NaN  NaN   left_only
# 4   K1   K0  NaN  NaN   C1   D1  right_only
# 5   K3   K0  NaN  NaN   C3   D3  right_only

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['K0', 'K2', 'K2'])
print(left)
#      A   B
# K0  A0  B0
# K1  A1  B1
# K2  A2  B2
print(right)
#      C   D
# K0  C0  D0
# K2  C1  D1
# K2  C2  D2

res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
#      A   B    C    D
# K0  A0  B0   C0   D0
# K1  A1  B1  NaN  NaN
# K2  A2  B2   C1   D1
# K2  A2  B2   C2   D2

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boys', '_girls'], how='outer')
print(res)
#     k  age_boys  age_girls
# 0  K0       1.0        4.0
# 1  K0       1.0        5.0
# 2  K1       2.0        NaN
# 3  K2       3.0        NaN
# 4  K3       NaN        6.0
