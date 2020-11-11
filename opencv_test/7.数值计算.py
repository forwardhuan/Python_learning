#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import os
from constants import res_image_path

img_cat = cv2.imread(os.path.join(res_image_path, 'cat.jpg'))

img_cat2 = img_cat + 10
# print(img_cat2[:5, :, 0])

# numpy加法和cv2中的加法不同

# 相当于 %256
# print((img_cat + img_cat2)[:5, :, 0])

# 超过255取255
print(cv2.add(img_cat, img_cat2)[:5, :, 0])
