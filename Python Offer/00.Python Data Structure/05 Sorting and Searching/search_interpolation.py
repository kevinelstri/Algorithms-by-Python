# coding:utf-8

'''
插值算法: O(n)
对于表内数据量较大，且关键字分布比较均匀的查找表，使用插值算法的平均性能比二分查找要好得多；
而对于分布极端不均匀的数据，就不适合使用插值算法
'''


def interpolartion(array, num):
    first = 0
    last = len(array) - 1
    count = 0
    while first <= last:
        count += 1
        mid = first + int((last - first) * (num - array[first]) / (array[last] - array[first]))
        if array[mid] == num:
            return True
        if array[mid] < num:
            first = mid + 1
        if array[mid] > num:
            last = mid - 1
    return False


if __name__ == '__main__':
    array = [1, 5, 7, 8, 22, 54, 99, 123, 200, 332]
    print interpolartion(array, 22)
