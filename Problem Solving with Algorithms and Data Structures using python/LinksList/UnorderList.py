# coding:utf-8

from Node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
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

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == item and previous is None:
                self.head = current.get_next()
            else:
                previous = current
                current = current.get_next()
                while current.get_data() == item:
                    previous.set_next(current.get_next())
            return True
        return False

    # def add_item(self, pos, item):
    #     current = self.head
    #     i = 0
    #     if current.get_next is None:
    #         current.set_next(pos)
    #         current.set_data(item)
    #     else:
    #         while i <= pos:
    #             current = current.get_next()
    #             i += 1
    #         previous = current
    #         post = current.get_next()
    #         previous.set_next(pos)
    #         previous.set_data(item)
    #         current = previous.get_next()
    #         current.set_next(post)


L = UnorderedList()
L.add(8)
# print L.size()
L.add(9)
L.add(10)
L.add(11)
L.add(13)
L.add(73)
L.add(432)
print L.size()
# print L.search(41)
# print L.is_empty()
# print L.search(13)
print L.remove(8)
print L.size()
