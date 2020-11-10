#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2

img = cv2.imread('../resource/image/cat.jpg')
screen_shot = img[0:100, 0:100]
cv2.imshow('screen_shot', screen_shot)
cv2.waitKey(0)
cv2.destroyAllWindows()
