#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

# 生成随机浮点数, [0,1)
print(random.random())

# 生成区间浮点数，区间可以不是整数
print(random.uniform(1.2, 5.9))

# 生成0到10之间的一个整数型随机数
print(random.randint(0, 10))

# 生成从0到100的随机偶数
print(random.randrange(0, 100, 2))
# 生成从0到100的随机奇数：
print(random.randrange(1, 101, 2))

# 从一个序列中随机取出一个元素
print(random.choice('abcdefg'))

# 多个字符中生成指定数量的随机字符：
print(random.sample('abcdefghigklmn', 5))

# 打乱列表中元素的顺序
li = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(li)
print(li)
