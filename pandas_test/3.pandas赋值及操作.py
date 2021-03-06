#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

dates = np.arange(20170101, 20170107)
df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df1)
#            A   B   C   D
# 20170101   0   1   2   3
# 20170102   4   5   6   7
# 20170103   8   9  10  11
# 20170104  12  13  14  15
# 20170105  16  17  18  19
# 20170106  20  21  22  23

df1.iloc[2, 2] = 100
print(df1)
#            A   B    C   D
# 20170101   0   1    2   3
# 20170102   4   5    6   7
# 20170103   8   9  100  11
# 20170104  12  13   14  15
# 20170105  16  17   18  19
# 20170106  20  21   22  23

df1.loc[20170102, 'B'] = 200
print(df1)
#            A    B    C   D
# # 20170101   0    1    2   3
# # 20170102   4  200    6   7
# # 20170103   8    9  100  11
# # 20170104  12   13   14  15
# # 20170105  16   17   18  19
# # 20170106  20   21   22  23

df1[df1.A > 10] = 0
print(df1)
#           A    B    C   D
# 20170101  0    1    2   3
# 20170102  4  200    6   7
# 20170103  8    9  100  11
# 20170104  0    0    0   0
# 20170105  0    0    0   0
# 20170106  0    0    0   0

df1.A[df1.A == 0] = 1
print(df1)
#           A    B    C   D
# 20170101  1    1    2   3
# 20170102  4  200    6   7
# 20170103  8    9  100  11
# 20170104  1    0    0   0
# 20170105  1    0    0   0
# 20170106  1    0    0   0

# 添加一列
df1['E'] = 10
print(df1)
#           A    B    C   D   E
# 20170101  1    1    2   3  10
# 20170102  4  200    6   7  10
# 20170103  8    9  100  11  10
# 20170104  1    0    0   0  10
# 20170105  1    0    0   0  10
# 20170106  1    0    0   0  10

df1['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print(df1)
#           A    B    C   D   E  F
# 20170101  1    1    2   3  10  1
# 20170102  4  200    6   7  10  2
# 20170103  8    9  100  11  10  3
# 20170104  1    0    0   0  10  4
# 20170105  1    0    0   0  10  5
# 20170106  1    0    0   0  10  6

# 添加一行
df1.loc[20170107, ['A', 'B', 'C']] = [1, 2, 3]
print(df1)
#             A      B      C     D     E    F
# 20170101  1.0    1.0    2.0   3.0  10.0  1.0
# 20170102  4.0  200.0    6.0   7.0  10.0  2.0
# 20170103  8.0    9.0  100.0  11.0  10.0  3.0
# 20170104  1.0    0.0    0.0   0.0  10.0  4.0
# 20170105  1.0    0.0    0.0   0.0  10.0  5.0
# 20170106  1.0    0.0    0.0   0.0  10.0  6.0
# 20170107  1.0    2.0    3.0   NaN   NaN  NaN

s1 = pd.Series([1,2,3,4,5,6], index=['A','B','C','D','E','F'])
s1.name = 'S1'
df2=df1.append(s1)
print(df2)
#             A      B      C     D     E    F
# 20170101  1.0    1.0    2.0   3.0  10.0  1.0
# 20170102  4.0  200.0    6.0   7.0  10.0  2.0
# 20170103  8.0    9.0  100.0  11.0  10.0  3.0
# 20170104  1.0    0.0    0.0   0.0  10.0  4.0
# 20170105  1.0    0.0    0.0   0.0  10.0  5.0
# 20170106  1.0    0.0    0.0   0.0  10.0  6.0
# 20170107  1.0    2.0    3.0   NaN   NaN  NaN
# S1        1.0    2.0    3.0   4.0   5.0  6.0


# 插入列
df1.insert(1,'G',df2['E']) # 在df1为1的位置插入df2中E的列
print(df1)
#             A     G      B      C     D     E    F
# 20170101  1.0  10.0    1.0    2.0   3.0  10.0  1.0
# 20170102  4.0  10.0  200.0    6.0   7.0  10.0  2.0
# 20170103  8.0  10.0    9.0  100.0  11.0  10.0  3.0
# 20170104  1.0  10.0    0.0    0.0   0.0  10.0  4.0
# 20170105  1.0  10.0    0.0    0.0   0.0  10.0  5.0
# 20170106  1.0  10.0    0.0    0.0   0.0  10.0  6.0
# 20170107  1.0   NaN    2.0    3.0   NaN   NaN  NaN

# 移动位置
g = df1.pop('G')
df1.insert(6,'G',g)
print(df1)
#             A      B      C     D     E    F     G
# 20170101  1.0    1.0    2.0   3.0  10.0  1.0  10.0
# 20170102  4.0  200.0    6.0   7.0  10.0  2.0  10.0
# 20170103  8.0    9.0  100.0  11.0  10.0  3.0  10.0
# 20170104  1.0    0.0    0.0   0.0  10.0  4.0  10.0
# 20170105  1.0    0.0    0.0   0.0  10.0  5.0  10.0
# 20170106  1.0    0.0    0.0   0.0  10.0  6.0  10.0
# 20170107  1.0    2.0    3.0   NaN   NaN  NaN   NaN

# 删除一列
del df1['G']
print(df1)
#             A      B      C     D     E    F
# 20170101  1.0    1.0    2.0   3.0  10.0  1.0
# 20170102  4.0  200.0    6.0   7.0  10.0  2.0
# 20170103  8.0    9.0  100.0  11.0  10.0  3.0
# 20170104  1.0    0.0    0.0   0.0  10.0  4.0
# 20170105  1.0    0.0    0.0   0.0  10.0  5.0
# 20170106  1.0    0.0    0.0   0.0  10.0  6.0
# 20170107  1.0    2.0    3.0   NaN   NaN  NaN

df2 = df1.drop(['A','B'], axis=1)
print(df2)
#               C     D     E    F
# 20170101    2.0   3.0  10.0  1.0
# 20170102    6.0   7.0  10.0  2.0
# 20170103  100.0  11.0  10.0  3.0
# 20170104    0.0   0.0  10.0  4.0
# 20170105    0.0   0.0  10.0  5.0
# 20170106    0.0   0.0  10.0  6.0
# 20170107    3.0   NaN   NaN  NaN

df2 = df1.drop([20170101, 20170102], axis=0)
print(df2)
#             A    B      C     D     E    F
# 20170103  8.0  9.0  100.0  11.0  10.0  3.0
# 20170104  1.0  0.0    0.0   0.0  10.0  4.0
# 20170105  1.0  0.0    0.0   0.0  10.0  5.0
# 20170106  1.0  0.0    0.0   0.0  10.0  6.0
# 20170107  1.0  2.0    3.0   NaN   NaN  NaN