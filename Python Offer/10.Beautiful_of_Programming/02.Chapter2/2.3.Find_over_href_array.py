# coding:utf-8

'''
2.3寻找发帖水王
实质上：在一个数组中找出出现次数大于数组长度一半的一个数字
（1）排序，查找
（2）排序+二分法n/2
（3）hash计数
（4）每次删除两个不同的数
'''
from collections import Counter


# 排序
def sorted(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


# 二分法：只需要取一次中间数值即可
def binary(array):
    array = sorted(array)
    num = array[len(array) / 2]
    return num


# Main_Function
def FindNumber(array):
    num = binary(array)
    return num


if __name__ == '__main__':
    array = [3, 3, 2, 7, 3, 3, 3, 3, 3, 2, 7, 3, 3, 2, 3, 4, 8, 3, 7, 3, 2, 8, 3, 6, 3, 3, 7, 4, 3, 4, 7, 3, 3, 3, 4, 8]

    # print len(array)
    # s = [ele for ele in array if ele == 3]
    # print len(s)
    print FindNumber(array)
    # 内置函数
    # c = Counter()
    # for i in array:
    #     c[i] = c[i] + 1
    # print c
