# coding:utf-8

'''
2.5寻找最大的K个数
注意：海量数据处理
（1）最大的K个数(0<k<n)
（2）第k到m大的数（0<k<=m<=n）
'''


# Question1:
def FindK(array, K):
    L = len(array)
    if K <= 0 or K > L:
        return None

    s = []
    for i in range(len(array)):
        if i < K:
            s.append(array[i])
        minNum = min(s)
        if array[i] > minNum:
            s.append(array[i])
            s.remove(minNum)
    return s


# Question2:
def Findkm(array, k, m):
    L = len(array)
    if k <= 0 or k > L or m > L or k >= m or m <= 0:
        return None
    sk = []
    sm = []
    for i in range(L):
        if i < k:
            sk.append(array[i])
        if i < m:
            sm.append(array[i])
        if array[i] > min(sk):
            sk.append(array[i])
            sk.remove(min(sk))
        if array[i] > min(sm):
            sm.append(array[i])
            sm.remove(min(sm))
    s = [ele for ele in sm if ele not in sk]
    return s


if __name__ == '__main__':
    K = 5
    M = 10
    array = [1, 2, 332, 3, 13, 2, 3, 21, 3, 2, 3, 2, 32, 32325, 443, 53, 4]
    arrayMax = []
    for line in open('2.5.Random.txt').readlines():
        line = line.strip('\n')
        arrayMax.append(int(line))
    print Findkm(arrayMax, K, M)  # 海量数据处理：共有9999999个数字，求最大的K个数
    # print FindK(array, K)
