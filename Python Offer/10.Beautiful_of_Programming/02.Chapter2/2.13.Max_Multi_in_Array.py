# coding:utf-8

'''
2.13子数组的最大乘积
'''


# 乘积最大的两个数
def MaxMul(array):
    if array is None or len(array) == 0:
        return None
    Mul = array[0]
    result = 0
    for i in range(len(array)):
        Mul *= array[i]
        Mul = max(Mul, array[i])
        result = max(result, Mul)
    return result


def MxMul2(array):
    if array is None or len(array) == 0:
        return None
    Sum_0 = 0
    Sum_1 = 1
    Sum_2 = []
    for i in range(len(array)):
        if array[i] == 0:
            Sum_0 *= array[i]
        if array[i] > 0:
            Sum_1 *= array[i]
        if array[i] < 0:
            if len(Sum_2) == 3:
                min1 = min(Sum_2)
                Sum_2.remove(Sum_2.index(min1))
                min2 = min(Sum_2)
                Sum_2.remove(Sum_2.index(min2))
                Sum_1 *= (min1 * min2)
            else:
                Sum_2.append(array[i])
    print Sum_1
    print Sum_2
    if len(Sum_2) == 2:
        Sum_1 *= (Sum_2[0] * Sum_2[1])
    return Sum_1


if __name__ == '__main__':
    array = [1, 2, -1, 3, 4, -2, 5, -3]
    # print MaxMul(array)
    print MxMul2(array)
