# coding:utf-8

'''
二分查找
'''


def binarysearch(array, num):
    first = 0
    last = len(array) - 1

    while first < last:
        mid = (first + last) / 2
        if array[mid] > num:
            last = mid - 1
        elif array[mid] < num:
            first = mid + 1
        else:
            return mid + 1
    return -1


if __name__ == '__main__':
    number = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
    num = 7
    print binarysearch(number, num)
