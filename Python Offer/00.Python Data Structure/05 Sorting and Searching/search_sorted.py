# coding:utf-8

'''
有序表查找：二分查找

'''


def binarySearch(array, num):
    first = 0
    last = len(array) - 1
    count = 0
    while first <= last:
        count += 1
        mid = first + last
        if array[mid] == num:
            return True
        if array[mid] > num:
            last = mid-1
        if array[mid] < num:
            first = mid+1
    else:
        return False


if __name__ == '__main__':
    array = [1, 5, 7, 8, 22, 54, 99, 123, 200, 332]
    print binarySearch(array, 332)
