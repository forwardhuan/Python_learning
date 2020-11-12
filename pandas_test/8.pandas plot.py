#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data = data.cumsum()
# print(data)
# data.plot()
# plt.show()

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=['A', 'B', 'C', 'D'])
data = data.cumsum()
print(data.head())
# data.plot()
# plt.show()

ax = data.plot.scatter(x='A', y='B', color='Blue', label='class 1')
data.plot.scatter(x='A', y='C', color='Green', label='class 2', ax=ax)
plt.show()
