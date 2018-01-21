# coding:utf-8

'''
2.14 求数组的子数组之和的最大值
'''


def seqsum(array, first, last):
    sum = 0
    for i in range(first, last + 1):
        sum += array[i]
    return sum


def maxnum(a, b):
    if a >= b:
        return a
    else:
        return b


# 原始方法：将所有子数组之和都计算出来，求最大值
def MaxSum(array):
    if array is None or len(array) == 0:
        return None
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum = seqsum(array, i, j)
            result.append(sum)
    return max(result)


# 减少循环
def MaxSum2(array):
    if array is None or len(array) == 0:
        return None
    result = []
    for i in range(len(array)):
        sum = array[0]
        for j in range(i + 1, len(array)):
            sum += array[j]
            result.append(sum)
    return result


# 递归:找规律
# 前面之和<下一个数字，前面之和删除
# 遇到下一个负数时，记录前面的最大值，不断比较
def MaxSum3(array):
    if array is None or len(array) == 0:
        return None
    sum = 0
    sumTag = 0
    for i in range(len(array)):
        if sum + array[i] < array[i]:
            sum = array[i]
            sumTag = array[i]
        elif array[i] < 0:
            sum += array[i]
        else:
            sum += array[i]
            if sum > sumTag:
                sumTag = sum
        if sumTag < sum:
            sumTag = sum
        print 'TAG:', sumTag
        print 'SUM:', sum
        print '------------'
    return sumTag


if __name__ == '__main__':
    array = [5, 6, -2, 3, -4, 9, 2, 3, 8, -5, -5, 18]
    print MaxSum3(array)
