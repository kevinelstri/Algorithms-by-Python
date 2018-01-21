# coding:utf-8

'''
和为S的数字
1、输入一个递增排序的数组和一个数字S， 查找两个数字，使得它们的和正好为S
2、输入一个正数S， 打印出所有和为S的连续正数序列
'''

'''
1、双指针
'''


# 1、双指针
def FindNumberWithSum(array, k):
    if array is None or len(array) == 0:
        return None
    first = 0
    last = len(array) - 1
    while first < last:
        if array[first] + array[last] == k:
            print array[first], array[last]
            first += 1
            last -= 1
        elif array[first] + array[last] > k:
            last -= 1
        else:
            first += 1
    return -1


# 2、双指针，两个指针不断后移，来计算序列的和
def FindContinueSequence(n):
    if n <= 2:
        return None
    # if n / 2 + n / 2 + 1 == n:
    #     print n / 2, (n / 2 + 1)
    first = 1
    last = 2
    CSum = ContinueSum(first, last)
    while first < n / 2:
        if CSum == n:
            Continue(first, last)
            first += 1
        while CSum > n and first < n / 2:
            CSum -= first
            first += 1
            if CSum == n:
                Continue(first, last)
                first += 1
        last += 1
        CSum = ContinueSum(first, last)
    return None


def ContinueSum(first, last):
    sum = 0
    for i in range(first, last + 1):
        sum += i
    return sum


def Continue(first, last):
    for i in range(first, last + 1):
        print i,
    print


if __name__ == '__main__':
    k = 15
    array = [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 15]
    n = 27
    # FindNumberWithSum(array, k)
    FindContinueSequence(n)
    # print ContinueSum(1, 10)
    # Continue(1, 10)
