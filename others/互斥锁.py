#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import threading


def sorry():
    print('我错了')
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=sorry).start()
