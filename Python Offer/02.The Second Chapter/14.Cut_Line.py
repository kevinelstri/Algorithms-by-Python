# coding:utf-8

'''
剪绳子
给一根长度为n的绳子，把绳子剪成m段，每段长度分别为k[0],k[1],k[2]...,求它们的最大乘积是多少？
'''

'''
递归：自上而下，会有重复操作
动态规划：自下而上，不会有重复
'''

'''
分析：
当 length=2, 1+1, f(2)=1
当 length=3, 1+1+1,1+2, f(3)=2
当 length>4时，可以将绳子的长度剪切为小于length的长度，
换句话说，也就是可以使用较小的长度剪切来表示较大的长度剪切，
所以在计算length=n的长度乘积时，可以通过自下而上的动态规划来求解，
不断计算长度较小的绳子的剪切乘积值，来获取最大的乘积值。
'''


def MaxResult(length):
    if length == 0:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    s = [0, 1, 2, 3]  # 任意长度最大乘积值的存储

    # 长度小于等于3的绳子的结果是初始值
    for i in range(4, (length + 1)):
        maxvalue = []  # 对于每个长度的绳子，初始乘积最大值都为0
        for j in range(1, i / 2):
            value = s[j] * s[i - j]  # j+i-j=i,通过小问题求解大问题
            maxvalue.append(value)
        s.append(max(maxvalue))
    return s


if __name__ == '__main__':
    length = 20
    print MaxResult(length)
