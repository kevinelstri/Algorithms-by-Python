# coding:utf-8

'''
《算法导论》chapter15--动态规划
钢条切割：
对长度为n的钢条进行切割，使能获得更大的利润
长度：1 2 3 4 5  6  7  8  9  10
价格：1 5 8 9 10 17 17 20 24 30
'''


def MaxCut(length):
    if length < 1:
        return 0
    if length == 1:
        return 0
    if length == 2:
        return 5
    if length == 3:
        return 8

    realvalue = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    real = [0, 1, 5, 8]
    for i in range(4, length + 1):
        maxValue = []
        for j in range(1, i / 2):
            value = realvalue[j] + realvalue[i - j]
            maxValue.append(value)
        real.append(max(maxValue))
    return real


if __name__ == '__main__':
    length = 11
    print MaxCut(length)
