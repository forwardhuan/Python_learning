#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.arange(24, 36).reshape((3, 4)), columns=['a', 'b', 'c', 'd'])
print(df1)
#    a  b   c   d
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
print(df2)
#     a   b   c   d
# 0  12  13  14  15
# 1  16  17  18  19
# 2  20  21  22  23
print(df3)
#     a   b   c   d
# 0  24  25  26  27
# 1  28  29  30  31
# 2  32  33  34  35


df4 = pd.concat([df1, df2, df3], axis=0)  # 纵向合并
print(df4)
#     a   b   c   d
# 0   0   1   2   3
# 1   4   5   6   7
# 2   8   9  10  11
# 0  12  13  14  15
# 1  16  17  18  19
# 2  20  21  22  23
# 0  24  25  26  27
# 1  28  29  30  31
# 2  32  33  34  35

# 纵向合并，不考虑原来的index
df4 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(df4)
#     a   b   c   d
# 0   0   1   2   3
# 1   4   5   6   7
# 2   8   9  10  11
# 3  12  13  14  15
# 4  16  17  18  19
# 5  20  21  22  23
# 6  24  25  26  27
# 7  28  29  30  31
# 8  32  33  34  35

# 横向合并
df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)
#    a  b   c   d   a   b   c   d   a   b   c   d
# 0  0  1   2   3  12  13  14  15  24  25  26  27
# 1  4  5   6   7  16  17  18  19  28  29  30  31
# 2  8  9  10  11  20  21  22  23  32  33  34  35

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['a', 'b', 'c', 'f'])
print(df1)
#    a  b   c   f
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['a', 'c', 'd', 'e'])
print(df2)
#     a   c   d   e
# 0  12  13  14  15
# 1  16  17  18  19
# 2  20  21  22  23

# 合并两个表，缺少的部分填充NaN
df4 = pd.concat([df1, df2], join='outer', ignore_index=True)
print(df4)
#     a    b   c     f     d     e
# 0   0  1.0   2   3.0   NaN   NaN
# 1   4  5.0   6   7.0   NaN   NaN
# 2   8  9.0  10  11.0   NaN   NaN
# 3  12  NaN  13   NaN  14.0  15.0
# 4  16  NaN  17   NaN  18.0  19.0
# 5  20  NaN  21   NaN  22.0  23.0

# 只合并相同的部分，缺少的部分去掉
df4 = pd.concat([df1, df2], join='inner', ignore_index=True)
print(df4)
#     a   c
# 0   0   2
# 1   4   6
# 2   8  10
# 3  12  13
# 4  16  17
# 5  20  21


df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['a', 'b', 'c', 'f'])
print(df1)
#    a  b   c   f
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
df2 = pd.DataFrame(np.arange(12, 24).reshape((4, 3)), columns=['a', 'c', 'd'])
print(df2)
#     a   c   d
# 0  12  13  14
# 1  15  16  17
# 2  18  19  20
# 3  21  22  23

df4 = pd.concat([df1, df2], axis=1)
print(df4)
#      a    b     c     f   a   c   d
# 0  0.0  1.0   2.0   3.0  12  13  14
# 1  4.0  5.0   6.0   7.0  15  16  17
# 2  8.0  9.0  10.0  11.0  18  19  20
# 3  NaN  NaN   NaN   NaN  21  22  23
