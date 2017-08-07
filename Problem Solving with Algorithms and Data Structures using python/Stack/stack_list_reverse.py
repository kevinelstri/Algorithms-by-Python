# coding:utf-8


# Stack: Reverse,add and remove in the first
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack()
s.push('x')
s.push('y')
s.pop()
s.push('z')
print s.peek()

m = Stack()
m.push('x')
m.push('y')
m.push('z')
print m.is_empty()
while not m.is_empty():
    m.pop()
print m.is_empty()

