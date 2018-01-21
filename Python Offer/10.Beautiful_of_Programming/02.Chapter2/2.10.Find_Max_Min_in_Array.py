# coding:utf-8

'''
2.10寻找数组中的最大值和最小值
（1）两个两个的比较,减少比较次数
（2）分治法比较，递归
'''


# 比较大小
def Compare(a, b):
    if a > b:
        return a, b
    elif a < b:
        return b, a
    else:
        return a, a


# 寻找数组最大最小值
def FindMaxMin(array):
    if array is None or len(array) == 0:
        return None
    length = len(array)
    L = len(array) / 2
    if L * 2 == length:
        Max, Min = Compare(array[0], array[1])
        for i in range(2, length, 2):
            max, min = Compare(array[i], array[i + 1])
            if max > Max:
                Max = max
            if Min > min:
                Min = min
        return Max, Min
    else:
        Max, Min = Compare(array[0], array[1])
        for i in range(2, length - 1, 2):
            max, min = Compare(array[i], array[i + 1])
            if max > Max:
                Max = max
            if Min > min:
                Min = min
        if Max < array[-1]:
            Max = array[-1]
        if Min > array[-1]:
            Min = array[-1]
        return Max, Min


# 分治法：递归
def SearchMaxMin(array):
    if array is None or len(array)==0:
        return None
    L = len(array) / 2
    if len(array) == 2:
        max, min = Compare(array[0], array[1])
        return max, min
    if len(array) == 1:
        return array[0], array[0]
    maxl, minl = SearchMaxMin(array[:L])
    maxr, minr = SearchMaxMin(array[L:])
    if maxl < maxr:
        max = maxr
    else:
        max = maxl
    if minl < minr:
        min = minl
    else:
        min = minr
    return max, min


if __name__ == '__main__':
    array = [5, 10, 8, 3, 7, 9]
    # print FindMaxMin(array)

    print SearchMaxMin(array)
