#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy  as np

dates = np.arange(20170101, 20170105)
df1 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=dates, columns=['A', 'B', 'C'])
print(df1)
#           A   B   C
# 20170101  0   1   2
# 20170102  3   4   5
# 20170103  6   7   8
# 20170104  9  10  11

df2 = pd.DataFrame(df1, index=dates, columns=['A', 'B', 'C', 'D', 'E'])
print(df2)
#           A   B   C   D   E
# 20170101  0   1   2 NaN NaN
# 20170102  3   4   5 NaN NaN
# 20170103  6   7   8 NaN NaN
# 20170104  9  10  11 NaN NaN

s1 = pd.Series([3, 4, 6], index=dates[:3])
s2 = pd.Series([32, 5, 2], index=dates[1:])
df2['D'] = s1
df2['E'] = s2
print(df2)
#           A   B   C    D     E
# 20170101  0   1   2  3.0   NaN
# 20170102  3   4   5  4.0  32.0
# 20170103  6   7   8  6.0   5.0
# 20170104  9  10  11  NaN   2.0

# 去除掉有空值的行
df3 = df2.dropna(axis=0, how='any')  # axis=[0,1] 0代表行，1代表列, how=['any','all'] any代表任意一个， all代表全部
print(df3)
#           A  B  C    D     E
# 20170102  3  4  5  4.0  32.0
# 20170103  6  7  8  6.0   5.0

# 去除掉有空值的列
df3 = df2.dropna(axis=1, how='any')
print(df3)
#           A   B   C
# 20170101  0   1   2
# 20170102  3   4   5
# 20170103  6   7   8
# 20170104  9  10  11

# 填充空值
df3 = df2.fillna(value=0)
print(df3)
#           A   B   C    D     E
# 20170101  0   1   2  3.0   0.0
# 20170102  3   4   5  4.0  32.0
# 20170103  6   7   8  6.0   5.0
# 20170104  9  10  11  0.0   2.0

# 判断空值
df3 = df2.isnull()
print(df3)
#               A      B      C      D      E
# 20170101  False  False  False  False   True
# 20170102  False  False  False  False  False
# 20170103  False  False  False  False  False
# 20170104  False  False  False   True  False

# 只要有一个空值就会返回True
df3 = np.any(df2.isnull())
print(df3)
# True

# 所有为空值返回True
df3 = np.all(df2.isnull())
print(df3)
# False
