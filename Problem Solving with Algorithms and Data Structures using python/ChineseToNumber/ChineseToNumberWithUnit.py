# coding:utf-8

import uniout
import numpy as np


class Stack:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# chinese to number : 五十三-->53， 一千二百四十九-->1249
def ChineseToNumber(ch_str):
    ch_str = ch_str.decode('utf8')
    c_n = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
           '百': 100, '千': 1000, '万': 10000, '亿': 100000000, '零': 0}

    n = 0
    for i in range(-1, -len(ch_str), -1):
        if c_n.has_key(ch_str[i].encode('utf8')) is False:  # 去除单位
            n += 1
    ch_string = ch_str[:-n]
    # print n
    # print ch_str
    # print ch_string

    number = []
    for i in range(len(ch_string)):
        num = c_n[ch_string[i].encode('utf8')]
        # print num
        number.insert(0, num)
    # print number

    # 数字组合
    stack = Stack()
    stack.push(number[0])
    for i in range(1, len(number)):
        if number[i] >= 10:
            stack.push(number[i])
        elif number[i] < 10 and number[i] != 0:
            s = stack.pop()
            s *= number[i]
            stack.push(s)
        else:
            i += 1

    sum = 0
    while stack.is_Empty() is False:
        sum += stack.peek()
        stack.pop()

    # print 'num:', n
    # print ch_str
    sum = str(sum)+ch_str[-n:]  # 添加单位
    print sum
    print '-------------------------'


if __name__ == '__main__':
    ch_string1 = '零个'
    ch_string2 = '十公顷'
    ch_string3 = '百双'
    ch_string4 = '三百二十三平方米'
    ch_string5 = '八万零三百二十三元'
    ch_string6 = '一亿零八万零三百二十三亩'
    ChineseToNumber(ch_string1)  # 汉字转数字
    ChineseToNumber(ch_string2)
    ChineseToNumber(ch_string3)
    ChineseToNumber(ch_string4)
    ChineseToNumber(ch_string5)
    ChineseToNumber(ch_string6)

