#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
res_image_path = os.path.join(base_dir, 'resource/image')
res_video_path = os.path.join(base_dir, 'resource/video')
res_temp_path = os.path.join(base_dir, 'resource/temp')
res_file_path = os.path.join(base_dir, 'resource/file')

if os.path.exists(res_temp_path) is False:
    os.mkdir(res_temp_path)
