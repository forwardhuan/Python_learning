#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

print(re.search('asd', "Aasd"))
# <re.Match object; span=(1, 4), match='asd'>

# 前面的 字符串是规则(正则表达式)，后面字符串是被校验的字符串
print(re.findall("[A-Z]", 'ASDfghJK'))
# ['A', 'S', 'D', 'J', 'K']

print(re.findall("[A-Z]+", 'ASDfghJK'))
# ['ASD', 'JK']


# 找到a替换成A，在第三个字符串中查找"a"
# 建议在正则表达式中，被比较的字符串前加r，不用担心转义的问题
print(re.sub('a', 'A', 'abcdabcdds'))
# AbcdAbcdds



