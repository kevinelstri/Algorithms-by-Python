# coding:utf-8

'''
数值的整数次方
注意：底数的取值范围以及指数的取值范围
'''


def powNumber(m, n):
    if m == 0:
        return 0
    elif m != 0 and n == 0:
        return 1
    else:
        return pow(m, n)


if __name__ == '__main__':
    m, n = 0, 0
    m1, n1 = 0, -1
    m2, n2 = -1, 0
    m3, n3 = -1, -1
    m4, n4 = 2, -2
    print powNumber(m, n)
    print powNumber(m1, n1)
    print powNumber(m2, n2)
    print powNumber(m3, n3)
    print powNumber(m4, n4)
