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
def ChineseToNumber(ch_string):
    ch_string = ch_string.decode('utf8')
    c_n = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
           '百': 100, '千': 1000, '万': 10000, '亿': 100000000, '零': 0}

    number = []
    for i in range(len(ch_string)):
        num = c_n[ch_string[i].encode('utf8')]
        # print num
        number.insert(0, num)
    print number

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
    print sum


if __name__ == '__main__':
    ch_string1 = '零'
    ch_string2 = '十'
    ch_string3 = '百'
    ch_string4 = '三百二十三'
    ch_string5 = '八万零三百二十三'
    ch_string6 = '一亿零八万零三百二十三'
    ChineseToNumber(ch_string1)  # 汉字转数字
    ChineseToNumber(ch_string2)
    ChineseToNumber(ch_string3)
    ChineseToNumber(ch_string4)
    ChineseToNumber(ch_string5)
    ChineseToNumber(ch_string6)

