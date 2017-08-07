# coding:utf-8


# Stack:implement the stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items == []:
            return None
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# s = Stack()
# print s.peek()
