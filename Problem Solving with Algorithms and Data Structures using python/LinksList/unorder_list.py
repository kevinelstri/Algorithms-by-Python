# coding:utf-8


# The Unordered List ADT
class List_Unorder:
    def __init__(self):
        self.List = []

    def add_List(self, item):
        self.List.add(item)

    def remove_List(self, item):
        return self.List.remove(item)

    def search_List(self, item):
        if item in self.List:
            return True
        return False

    def is_empty(self):
        return self.List == []

    def size(self):
        return len(self.List)

    def append_List(self, item):
        self.List.append(item)

    def index_List(self, item):
        return self.List.index(item)

    def insert_List(self, pos, item):
        self.List.insert(pos, item)

    def pop(self):
        return self.List.pop()

    def popo(self, pos):
        return self.List.pop(pos)




