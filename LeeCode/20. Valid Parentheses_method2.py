# codinng:utf-8

class Solution:
    def isValid(self, s):
        items = []
        sym = {')': '(', ']': '[', '}': '{'}
        left = '([{'
        for ls in s:
            if ls in left:
                items.append(ls)
            elif items != [] and sym[ls] == items[-1]:
                items.pop()
            else:
                return False
        return items == []

s = Solution()
print s.isValid('(({))')
