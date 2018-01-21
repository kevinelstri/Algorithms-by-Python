# coding:utf-8

'''
2.1子数组之和的最大值（二维）
（1）直接遍历求和，比较所有的大小
（2）建立二维数组来保存部分和
'''


def Sum(array, i_min, i_max, j_min, j_max):
    sum = 0
    for i in range(i_min, i_max + 1):
        for j in range(j_min, j_max + 1):
            sum += array[i][j]
    return sum


# Method1:最直接的方法直接遍历求和
def MaxSum(array):
    if array is None or len(array) == 0:
        return None
    maxSum = 0
    for i_min in range(len(array)):
        for i_max in range(i_min, len(array)):
            for j_min in range(len(array[0])):
                for j_max in range(j_min, len(array[0])):
                    maxSum = max(maxSum, Sum(array, i_min, i_max, j_min, j_max))
    return maxSum


# Method2:通过矩阵相加减，使用部分和来达到目的
def MaxSum2(array):
    if array is None or len(array) == 0:
        return None
    p = Partion(array)
    maxSum = 0
    for i_min in range(len(array)):
        for i_max in range(i_min + 1, len(array)):
            for j_min in range(len(array[0])):
                for j_max in range(j_min + 1, len(array[0])):
                    # print p[i_max][j_max]
                    if i_min == 0 and j_min == 0:
                        result = p[i_max][j_max]
                    if i_min == 0:
                        result = p[i_max][j_max] - p[i_min - 1][j_max]
                    if j_min == 0:
                        result = p[i_max][j_max] - p[i_max][j_min - 1]
                    elif i_min != 0 and j_min != 0:
                        result = p[i_max][j_max] - p[i_max][j_min - 1] - p[i_min - 1][j_max] + p[i_min - 1][j_min - 1]
                    print i_min, j_min, i_max, j_max, result
                    maxSum = max(maxSum, result)
    return maxSum


# 求解部分和，注意python对二维数组的创建
def Partion(array):
    p = [[] for i in range(len(array))]  # 二维数组的创建，必须使用for循环来创建
    p[0].append(array[0][0])
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if i == 0 and j > 0:
                p[0].append(array[i][j] + p[i][j - 1])
            if j == 0 and i > 0:
                p[i].append(array[i][j] + p[i - 1][j])
            if j > 0 and i > 0:
                p[i].append(array[i][j] + p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1])
    print p
    return p


if __name__ == '__main__':
    array = [[10, 2, 3],
             [2, 3, -4],
             [4, 5, 6]]
    print MaxSum(array)
    # print Partion(array)
    print MaxSum2(array)
