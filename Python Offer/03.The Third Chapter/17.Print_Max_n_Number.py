# coding:utf-8

'''
打印最大的n位数
注意：python支持无限精度的整数运算
'''


def print_number(n):
    maxNumber = pow(10, n)
    i = 1
    while i < maxNumber:
        print i,
        i += 1


if __name__ == '__main__':
    n = 20
    print_number(n)
