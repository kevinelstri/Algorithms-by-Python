# coding:utf-8

'''
翻转字符串：
1、翻转单词顺序, 翻转单词，保持单词顺序不变
2、左旋转字符串，将字符串左边k个字符移动到字符串最右端
'''


def ReverseWordString(str):
    if str is None or len(str) == 0:
        return None
    str = list(str)
    first = 0
    last = len(str) - 1
    while first <= last:
        temp = str[first]
        str[first] = str[last]
        str[last] = temp
        first += 1
        last -= 1
    # print str
    str = ''.join(seg for seg in str)
    return str


# 1、翻转单词顺序
def ReverseWord(str):
    str = str.split(' ')
    s = ''
    for seg in str:
        # print 'seg:', seg
        seg = ReverseWordString(seg)
        seg = seg + ' ',
        s += ' '.join(seg)
    return s


# 2、左旋转字符串(使用python内置函数)
def ReverseLeft(str, k):
    if str is None or len(str) == 0:
        return None
    if k <= 0 or k == len(str):
        return str
    if k > len(str):
        return False
    str = list(str)
    while k > 0:
        str.append(str[0])
        str.pop(0)
        k -= 1
    s =''
    s += ''.join(seg for seg in str)
    print s


# 2、左旋转字符串(使用翻转函数来实现左翻转)
def ReverseLeft2(str, k):
    if str is None or len(str) == 0:
        return None
    if k <= 0:
        return str
    if k > len(str):
        return False
    str = list(str)
    str1 = ReverseWordString(str[:k])
    str2 = ReverseWordString(str[k:])
    str1 += ''.join(str2)
    result = ReverseWordString(str1)
    return result


if __name__ == '__main__':
    str = 'I am a student'
    str2 = 'abcdefghijklmn'
    # print ReverseWord(str)
    k = 3
    ReverseLeft(str2, k)
    print ReverseLeft2(str2, k)
