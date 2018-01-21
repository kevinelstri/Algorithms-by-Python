# coding:utf-8

'''
《编程之美》
2.1求二进制中1的个数
对于一个无符号整形变量，求其二进制中1的个数
'''


def NumberOfBinary(n):
    if n == 0:
        return 0
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


if __name__ == '__main__':
    n = 0
    print NumberOfBinary(n)
