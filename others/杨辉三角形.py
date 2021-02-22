#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def triangle(n):
    row = [1] * n
    for i in range(n):
        old = 1
        for j in range(i // 2):
            next_index = j + 1
            val = old + row[next_index]
            old = row[next_index]
            row[next_index] = val
            if i != next_index * 2:
                row[i - next_index] = val
        s = "  " * (n - i - 1)
        print(s, row[:i + 1])


if __name__ == '__main__':
    triangle(10)

    #                    [1]
    #                  [1, 1]
    #                [1, 2, 1]
    #              [1, 3, 3, 1]
    #            [1, 4, 6, 4, 1]
    #          [1, 5, 10, 10, 5, 1]
    #        [1, 6, 15, 20, 15, 6, 1]
    #      [1, 7, 21, 35, 35, 21, 7, 1]
    #    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    #  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
