# coding:utf-8

'''
栈的建立
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(4)
    s.push(7)
    print(s.pop())
    print(s.peek())
    print(s.size())

