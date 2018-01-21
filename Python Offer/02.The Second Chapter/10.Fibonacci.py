# coding:utf-8

'''
斐波那契数列：f(n)=f(n-1)+f(n-2)
f(0) = 0
f(1) = 1
使用正方向进行计算斐波那契数列，可以避免重复元素产生

递归：对元素进行自函数处理，逆序操作
循环：对整个数组、列表或字符串进行操作，可以正向操作，也可以逆向操作
'''


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        first = 0
        second = 1
        count = 1
        while count < n:
            sum = first + second
            first = second
            second = sum
            count += 1
        return second


if __name__ == '__main__':
    for i in range(10):
        print fib(i),
