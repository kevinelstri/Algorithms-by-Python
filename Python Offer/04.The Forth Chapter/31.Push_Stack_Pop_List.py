# coding:utf-8

'''
栈的压入，弹出序列
第一个序列：栈的压入顺序
判断->第二个序列：栈的弹出顺序
假设栈中所有数字均不相同
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# 将弹出序列写入到栈中，对压入序列进行运算，比较与弹出序列之间的关系
def is_push(PushList, PopList):
    if len(PushList) <= 0 or len(PopList) <= 0:
        return False
    for i in range(len(PopList) - 1, -1, -1):
        t.push(PopList[i])
    # print t.peek()
    for i in range(len(PushList)):
        if PushList[i] != t.peek():
            s.push(PushList[i])
        elif PushList[i] == t.peek():
            t.pop()
    # print s.size()
    # print t.size()
    for i in range(s.size()):
        if s.peek() == t.peek():
            s.pop()
            t.pop()
        else:
            return False
    return t.is_empty()


if __name__ == '__main__':
    s = Stack()
    t = Stack()
    PushList = [1, 2, 3, 4, 5]
    PopList = [1, 5, 4, 3, 2]
    x = []
    y = []
    m = [1]
    n = [1]
    print is_push(PushList, PopList)
    print is_push(x, y)
    print is_push(m, n)
