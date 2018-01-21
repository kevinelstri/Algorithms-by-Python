# coding:utf-8

'''
求旋转数组的最小值
'''


def min(array):
    if len(array) <= 0 | (array == None):
        return None
    first = 0
    last = len(array) - 1
    mid = (first + last) / 2
    if first == last:
        return array[first]

    while first + 1 != last:
        if array[mid] > array[first] and array[mid] > array[last]:
            first = mid
            mid = (first + last) / 2
        if array[mid] < array[last] and array[mid] < array[first]:
            last = mid
            mid = (first + last) / 2
    return array[last]


if __name__ == '__main__':
    a = []
    b = [-1]
    array = [3, 4, 5, 0, 1, 2]
    array1 = [11, 13, 15, 19, 21, 1, 3, 5, 7]
    print min(a)
    print min(b)
    print min(array)
    print min(array1)
