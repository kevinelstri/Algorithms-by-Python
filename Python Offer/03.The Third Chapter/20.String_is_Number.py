# coding:utf-8

'''
判断字符串能不能表示数值
'''


def StringNumber(str):
    L = len(str)
    if L == 0:
        return False
    i = 0
    N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    F = ['+', '-']
    E = ['e', 'E']
    G = ['.']

    while i < L:
        if str[i] in N:
            i += 1
        elif str[i] in E:
            i += 1
            Number(str[i:])
        elif str[i] in F:
            i += 1
            Number(str[i:])
        elif str[i] in G:
            i += 1
            Number(str[i:])
        return False
    return False


def Number(str):
    N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while i < len(str):
        if str[i] not in N:
            return False
        else:
            i +=1
    return True


if __name__ == '__main__':
    str = '3+14'
    print StringNumber(str)
