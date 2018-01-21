# coding:utf-8

'''
剪绳子：
当 n>=5, 尽可能多的剪出长度为3的绳子；
当 n=4, 把绳子剪成长度为2的绳子
'''


def CutLine(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    if length == 4:
        return 2 * 2
    count3 = length / 3  # 除法
    count2 = (length - count3 * 3) / 2
    return int(pow(3, count3) * pow(2, count2))

    # 求余
    # pow(2, (num-num/n*n)/2)


if __name__ == '__main__':
    length = 10
    print CutLine(length)
