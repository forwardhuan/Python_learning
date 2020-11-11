#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import os
from constants import res_image_path

img = cv2.imread(os.path.join(res_image_path, "cat.jpg"))
top_s, bottom_s, left_s, right_s = (50, 50, 50, 50)
# 复制法，复制最边缘的像素
replicate = cv2.copyMakeBorder(img, top_s, bottom_s, left_s, right_s,
                               borderType=cv2.BORDER_REPLICATE)
# 反射法，以边缘像素开始，向两边复制，包含边缘部分，如fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img, top_s, bottom_s, left_s, right_s,
                             borderType=cv2.BORDER_REFLECT)
# 反射法，以边缘像素为轴，向两边复制，不包含边缘部分fedcb|abcdefg|fedcba
reflect101 = cv2.copyMakeBorder(img, top_s, bottom_s, left_s, right_s,
                                borderType=cv2.BORDER_REFLECT_101)
# 外包装法，cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(img, top_s, bottom_s, left_s, right_s,
                          borderType=cv2.BORDER_WRAP)
# 常量法，长数值填充
constant = cv2.copyMakeBorder(img, top_s, bottom_s, left_s, right_s,
                              borderType=cv2.BORDER_CONSTANT, value=(11, 33, 234))

plt.subplot(231), plt.imshow(img, 'Blues'), plt.title('original')
plt.subplot(232), plt.imshow(replicate, 'Blues'), plt.title('replicate')
plt.subplot(233), plt.imshow(reflect, 'Blues'), plt.title('reflect')
plt.subplot(234), plt.imshow(reflect101, 'Blues'), plt.title('reflect101')
plt.subplot(235), plt.imshow(wrap, 'Blues'), plt.title('wrap')
plt.subplot(236), plt.imshow(constant, 'Blues'), plt.title('constant')
plt.show()
