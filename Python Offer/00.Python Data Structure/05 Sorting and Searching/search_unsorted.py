# coding:utf-8

'''
无序表查找:顺序查找
顺序查找的时间复杂度，最好的情况就是O(1)，最差的情况就是O(n)，因此顺序查找时间复杂度为O(n)
'''


def sequential_search(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return True
    else:
        return False


if __name__ == '__main__':
    array = [1, 5, 8, 123, 22, 54, 7, 99, 200, 332]
    print sequential_search(array, 54)
