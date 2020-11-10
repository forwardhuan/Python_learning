#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2  # opencv默认读取的格式是BGR
import numpy
from matplotlib import pyplot as plt


def cv_show(name, image):
    # 图像的显示，也可以创建多个窗口
    cv2.imshow(name, image)
    # 等待时间，毫秒级，0表示任意键停止
    cv2.waitKey(0)
    # cv2.destroyAllWindows()


img = cv2.imread("../resource/image/cat.jpg")
# print(img)
print(img.shape)
# cv_show('image', img)

# 灰度图
img2 = cv2.imread('../resource/image/cat.jpg', cv2.IMREAD_GRAYSCALE)

print(img2.shape)
# 保存
cv2.imwrite('../resource/temp/cat.jpg', img2)

print(type(img2))
print(img2.size)
print(img2.dtype)
