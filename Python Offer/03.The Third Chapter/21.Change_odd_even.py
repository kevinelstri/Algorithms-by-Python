# coding:utf-8

'''
调整数组顺序使奇数位于偶数前面
'''


def changeOddEven(List):
    L = len(List)
    if L <= 0:
        return None
    i = 0
    j = L - 1
    while i <= j:
        if List[i] & 0x1 == 0 and List[j] & 0x1 != 0:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
        elif List[i] & 0x1 != 0:
            i += 1
        elif List[j] & 0x1 == 0:
            j -= 1
    return List


# 代码复用
def change(List):
    L = len(List)
    if L <= 0:
        return None
    i = 0
    j = L - 1
    while i <= j:
        if fun(List[i]) != 0:
            i += 1
        elif fun(List[j]) == 0:
            j -= 1
        else:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
    return List


def fun(i):
    return i & 0x1


if __name__ == '__main__':
    List1 = []
    List2 = [1, 2, 3, 4, 5, 6, 7]
    List3 = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    List4 = [1]
    List5 = [-2, -3, -4, 0, 2, 4]
    print changeOddEven(List1)
    print changeOddEven(List2)
    print changeOddEven(List3)
    print changeOddEven(List4)
    print changeOddEven(List5)
    print change(List2)
