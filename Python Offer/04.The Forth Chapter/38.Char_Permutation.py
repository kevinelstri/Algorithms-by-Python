# coding:utf-8

'''
给定一个字符串，打印所有字符之间的所有排列
'''


# 原始方法
def permutation(s):
    s = list(s)
    length = len(s)

    for i in range(length):
        for j in range(i, length):
            change(s[i], s[j])
            print s


def change(x, y):
    temp = x
    x = y
    y = temp



class Solution():
    # 递归思路
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()

        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))

            print i, ''.join(charList[:i]) + ''.join(charList[i + 1:])

            for j in temp:
                pStr.append(charList[i] + j)
        return pStr


if __name__ == '__main__':
    strs = 'abc'
    # print strs[1:2]
    permutation(strs)
    s = Solution()
    # s.Permutation(strs)
