#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def count(func):
    def wrapper(*args, **kwargs):
        print('start')
        func1 = func(*args, **kwargs)
        print("end")
        return func1

    return wrapper


@count
def sub():
    print('running')
    return "a"


print(sub())


