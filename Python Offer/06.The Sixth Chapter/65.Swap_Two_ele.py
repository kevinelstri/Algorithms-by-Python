# coding:utf-8

'''
交换两个变量的值
不能使用新的变量
'''


def SwapTwoEle(x, y):
    # 方法一：加减法
    x = x + y
    y = x - y
    x = x - y
    print x, y  # 交换

    # 方法二：异或法
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print x, y  # 交换


if __name__ == '__main__':
    x = 15
    y = 27
    SwapTwoEle(x, y)
