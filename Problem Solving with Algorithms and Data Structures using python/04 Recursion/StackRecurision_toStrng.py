# coding:utf-8

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def Stack_to_String(n, base):
    M = 'ABCDEF'
    if n < base and (base != 16):
        s.push(n)
    elif n < base and (base == 16):
        if n >= 10:
            s.push(M[n - 10])
        else:
            s.push(n)
    else:
        s.push(n % base)
        Stack_to_String(n / base, base)
    res = ''
    while not s.is_empty():
        res += str(s.pop())
    print res


n = 10
base = 16
s = Stack()
Stack_to_String(n, base)
