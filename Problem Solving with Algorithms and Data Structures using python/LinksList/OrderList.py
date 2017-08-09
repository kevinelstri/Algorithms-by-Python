# coding:utf-8

from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        self.head = temp
        current = self.head
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
            if (previous.get_data() < item) and (item <= current):
                previous.set_next(item)
                previous = previous.get_next()
                previous.set_next(current)
            else:
                current = current.get_next()
        current.set_next(item)

    def size(self):
        current = self.head
        print current.get_data()
        current = current.get_next()
        print current.get_data()
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
            return False
        return False




x = OrderedList()
print x.is_empty()
x.add(3)
x.add(7)
x.add(10)
x.add(13)
x.add(34)
x.add(5)
print x.is_empty()
print x.search(5)
print x.size()
