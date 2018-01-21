# coding:utf-8

'''
2.6 精确表达浮点数
0.9 = 9/10
0.33(3) = 1/3 = (33+3/9)/100
0.22(5) = (22+5/9)/100
'''
from __future__ import division


def FloatDouble(s):
    result = []
    s = s.split('.')
    first = int(s[0])  # 整数部分
    result.append(first)
    s = s[1]
    if '(' in s:
        s = s.split('(')
        second = s[0]  # 小数部分
        third = int(s[1][:-1])  # 循环部分
        result.append(second)
        result.append(third)
    else:
        second = s  # 小数部分
        third = 0
        result.append(second)
        result.append(third)
    # print result
    return result


def Result():
    result = FloatDouble(s)
    first = result[0]
    second = result[1]
    third = result[2]
    print first, second, third
    return first + float((int(second) + third / 9) / pow(10, len(second)))


if __name__ == '__main__':
    array = ['0.9', '0.3(3)', '0.22(5)', '2.33(4)']
    s = '2.33(4)'
    # s = '0.9'
    print Result()
