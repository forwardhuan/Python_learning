#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import os
import numpy as np
from constants import res_image_path

img = cv2.imread(os.path.join(res_image_path, 'cat.jpg'))

# # 均值滤波
# # 简单的平均卷积操作
blur = cv2.blur(img, (3, 3))
# cv2.imshow('blur',blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 方框滤波
# # 基本和均值一样，可以选择归一化
# box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# cv2.imshow('box', box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 方框滤波
# # 基本和均值一样，可以选择归一化, 容易越界
# box = cv2.boxFilter(img, -1, (3, 3), normalize=False)
# cv2.imshow('box', box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 高斯滤波
# 高斯模糊的卷积合理的数值是满足高斯分布，相当于更重视中间的
auusion = cv2.GaussianBlur(img, (5, 5), 1)
# cv2.imshow('auusion', auusion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 中值滤波
# 相当于用中值代替
median = cv2.medianBlur(img, 5)
# cv2.imshow('median', median)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 展示所有的
res = np.hstack((blur, auusion, median))
print(res)
cv2.imshow('median vs average', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
