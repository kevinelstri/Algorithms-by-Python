# coding:utf-8

'''
栈建立，在first进行压栈和出栈
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        if self.stack:
            return self.stack.pop(0)

    def peek(self):
        if self.stack:
            return self.stack[0]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s.size())
