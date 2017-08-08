# NO.20 Valid Parentheses

Question:

> Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
>
> The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.

Answer: (Method1)

~~~python
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

~~~

Result:

![20](C:\Users\kevinelstri\Desktop\20.png)

Answer: Method2

~~~python
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
~~~

Result:

![201](C:\Users\kevinelstri\Desktop\201.png)