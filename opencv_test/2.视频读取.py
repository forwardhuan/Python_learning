#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2  # opencv默认读取的格式是BGR
import os
from constants import res_video_path

print(res_video_path)
vc = cv2.VideoCapture(os.path.join(res_video_path, "test.mp4"))

# 检查是否打开正确
if vc.isOpened():
    is_open, frame = vc.read()
    while is_open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret is True:
            # 转换为灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)
            if cv2.waitKey(10) & 0xFF == 27:
                break
else:
    print("file can't be read")
vc.release()
cv2.destroyAllWindows()
