#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import os
from constants import res_file_path, res_temp_path

file = pd.read_csv(os.path.join(res_file_path, 'people.csv'), encoding='utf-8')
print(file)
#      姓名  年纪  分数
# 0  Jack  18  80
# 1   Tom  15  50
# 2  Jone  17  90

file.iloc[2, 0] = 'Jonee'
print(file)
#       姓名  年纪  分数
# 0   Jack  18  80
# 1    Tom  15  50
# 2  Jonee  17  90

file.to_csv(os.path.join(res_temp_path, 'people.csv'))
