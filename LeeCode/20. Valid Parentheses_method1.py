# coding:utf-8

# LeeCode NO.20
class Solution:
    def isValid(self, s):
        X = '([{'
        Y = ')]}'
        items = []
        for i in range(len(s)):
            if s[i] not in '([{})]':
                return False
            if s[i] in '([{':
                items.append(s[i])
            else:
                if items == []:
                    return False
                else:
                    if not X.index(items[-1]) == Y.index(s[i]):
                        return False
                    items.pop()
        return items == []


symbol_string = '['
so = Solution()
print so.isValid(symbol_string)
