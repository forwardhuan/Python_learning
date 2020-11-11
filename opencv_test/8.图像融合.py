#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import os
import matplotlib.pyplot as plt
from constants import res_image_path

img_cat = cv2.imread(os.path.join(res_image_path, 'cat.jpg'))
img_sen = cv2.imread(os.path.join(res_image_path, 'senery.jpg'))

# 需要两张图片的shape值相同才能相加
cat_shape = img_cat.shape
print(cat_shape)
print(img_sen.shape)
img_sen2 = cv2.resize(img_sen, (cat_shape[1], cat_shape[0]))
print(img_sen2.shape)

# res = cv2.addWeighted(img_cat, 0.4, img_sen2, 0.6, 0)
# plt.imshow(res)
# plt.show()

res = cv2.resize(img_cat, (0, 0), fx=3, fy=1)
print(res.shape)
plt.imshow(res)
plt.show()
