# coding:utf-8

'''
2.21连续加法
判断一个数是否可以使用连续数之和来表示
'''


# 计算序列之和
def seqsum(first, last):
    sum = 0
    for i in range(first, last + 1):
        sum += i
    return sum


# 打印找到的序列
def showseq(first, last):
    s = []
    for i in range(first, last + 1):
        s.append(i)
    return s


def SequenceAdd(n):
    if n <= 2:
        print None
    L = n / 2 + 2
    first = 1
    second = 2
    while first < second and (second <= L):
        sum = seqsum(first, second)
        if sum == n:
            print showseq(first, second)
            first += 1
            second += 1
        elif sum < n:
            second += 1
        else:
            first += 1
    print None


if __name__ == '__main__':
    for i in range(1001):
        print str(i)+':'
        SequenceAdd(i)
        print '---------------'
