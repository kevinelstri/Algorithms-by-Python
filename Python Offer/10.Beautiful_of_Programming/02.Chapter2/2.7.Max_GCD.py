# coding:utf-8

'''
2.7最大公约数问题
求两个正整数的最大公约数，如果两个正整数都很大，如何做？
'''


# 通过使用迭代减法来实现两个数字之间的最大公约数
def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
            gcd(m, n)
        if m < n:
            n = n - m
            gcd(n, m)
    if m == n:
        return m
    return m


if __name__ == '__main__':
    m = 120
    n = 27
    print gcd(m, n)
