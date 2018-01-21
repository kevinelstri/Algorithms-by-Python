# coding:utf-8

'''
产生随机数
'''

import numpy as np
import random


def RandomNumber():
    f = open('2.5.Random.txt', 'w')
    for i in range(9999999):
        f.write(str(random.randint(0, 999999999)))
        f.write('\n')


if __name__ == '__main__':
    RandomNumber()
