#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ret,dst = cv2,threshold(src, thresh, maxval, type)
# src:输入图，只能输入单通道的图像，通常来说为灰度图
# dst：输出图
# thresh：阈值
# maxval：当像素超过了阈值（或者小于阈值，根据type来决定）， 所赋予的值
# type：二值化操作的类型，包含以下五种类型
# cv2.THRESH_BINARY: 超过阈值部分取maxval（最大值），否则取0
# cv2.THRESH_BINARY_INV: THRESH_BINARY反转
# cv2.THRESH_TRUNC: 大于阈值部分设置为阈值，否则不变
# cv2.THRESH_TOZERO: 大于与之部分不变，否则设置为0
# cv2.THRESH_TOZERO_INV: THRESH_TOZERO的反转

import os
import cv2
import matplotlib.pyplot as plt

from constants import res_image_path

img_gray = cv2.imread(os.path.join(res_image_path, 'cat.jpg'), cv2.IMREAD_GRAYSCALE)

ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

title = ['origin', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']
images = [img_gray, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
