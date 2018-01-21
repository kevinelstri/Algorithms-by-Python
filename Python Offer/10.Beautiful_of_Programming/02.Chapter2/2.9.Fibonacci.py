# coding:utf-8

'''
2.9 斐波那契数列
（1）递归，从后向前，产生重复元素
（2）动态规划：从前向后
'''


def Fib(n):
    if n < 0:
        return None
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib


if __name__ == '__main__':
    n = 10
    print Fib(n)
