# coding:utf-8


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

# l = Node(3)
# l.set_next(4)
# l.set_next(5)
# l.set_next(4)
# l.set_next(6)
# print l.get_next()

