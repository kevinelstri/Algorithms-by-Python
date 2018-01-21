# coding:utf-8

'''
定义栈，实现一个求栈最小元素的min函数
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


if __name__ == '__main__':
    s = Stack()
    t = Stack()
    str = [4, 3, 5, 2, 10, 1, 8, 2]
    for i in range(len(str)):
        if s.is_empty():
            s.push(str[i])
            t.push(str[i])
        else:
            s.push(str[i])
            t.push(min(s.peek(), t.peek()))

    for i in range(len(str)):
        print s.pop(),
    print
    for i in range(len(str)):
        print t.pop(),
