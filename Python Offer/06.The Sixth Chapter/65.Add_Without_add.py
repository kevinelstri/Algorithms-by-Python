# coding:utf-8

'''
不用加减乘除法做加法运算
求两个整数之和，要求在函数体内不得使用+-*/四则运算
'''


def Add(x, y):
    sum = x ^ y
    carry = (x & y) << 1
    print sum, carry
    while carry != 0:
        Add(sum, carry)


if __name__ == '__main__':
    x = 15
    y = 27
    print Add(x, y)
