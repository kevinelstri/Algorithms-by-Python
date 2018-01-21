# coding:utf-8

'''
双端队列：允许两端都可以进行入队和出对的队列
'''


class Deque(object):
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def front(self, val):
        self.deque.insert(0, val)

    def rear(self, val):
        self.deque.append(val)

    def defront(self):
        if self.deque:
            return self.deque.pop(0)

    def derear(self):
        if self.deque:
            return self.deque.pop()

    def size(self):
        return len(self.deque)


if __name__ == '__main__':
    de = Deque()
    de.rear(2)
    de.rear(3)
    de.rear(4)
    de.front(5)
    de.front(6)
    de.front(7)
    print(de.size())
    print(de.derear())
    print(de.defront())
