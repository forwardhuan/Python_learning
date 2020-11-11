#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2
import os
from constants import res_image_path


def cv_show(name, image):
    # 图像的显示，也可以创建多个窗口
    cv2.imshow(name, image)
    # 等待时间，毫秒级，0表示任意键停止
    cv2.waitKey(0)
    # cv2.destroyAllWindows()


img = cv2.imread(os.path.join(res_image_path, "cat.jpg"))
b, g, r = cv2.split(img)

print(b.shape)
print(g.shape)
print(r.shape)

img2 = cv2.merge((b, g, r))
print(img2.shape)

# # 只保留R
# cur_img = img2.copy()
# cur_img[:, :, 0] = 0
# cur_img[:, :, 1] = 0
# cv_show('R', cur_img)
#
# # 只保留G
# cur_img = img2.copy()
# cur_img[:, :, 0] = 0
# cur_img[:, :, 2] = 0
# cv_show('R', cur_img)

# 只保留B
cur_img = img2.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0
cv_show('R', cur_img)
