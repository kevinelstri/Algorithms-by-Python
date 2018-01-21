# coding:utf-8

'''
匹配正则表达式：
模式中字符为'.'表示任意一个字符，模式中字符为'*'表示前面的字符出现任意次，包括0次
'''


def matchRegex(s, pattern):
    L1 = len(s)
    L2 = len(pattern)
    i, j = 0, 0
    temp = L2
    while i >= 0 and (j >= 0) and (i < L1) and j < L2:
        if s[i] == pattern[j]:
            i += 1
            j += 1
        elif s[i] != pattern[j] and pattern[j] == '.':
            i += 1
            j += 1
        elif s[i] != pattern[j] and pattern[j] == '*':
            if j - 1 < 0:
                return False
            elif s[i] == pattern[j - 1]:
                i += 1
            else:
                j += 1
                temp -= 1
        else:
                j += 1
                temp -= 2

    return L1 == temp


if __name__ == '__main__':
    s = 'aaa'
    pattern1 = 'ab*ab*a'
    pattern2 = 'aa.a'
    pattern3 = 'aa*'
    pattern4 = '.aa.'
    pattern5 = '*aa'

    s1 = ' '
    pattern6 = '.'
    pattern7 = ''
    pattern8 = ' '

    print matchRegex(s, pattern1)
    print matchRegex(s, pattern2)
    print matchRegex(s, pattern3)
    print matchRegex(s, pattern4)
    print matchRegex(s, pattern5)
    print '---------------------'
    print matchRegex(s1, pattern6)
    print matchRegex(s1, pattern7)
    print matchRegex(s1, pattern8)
