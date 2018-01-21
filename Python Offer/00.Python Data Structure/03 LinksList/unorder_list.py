# coding:utf-8

class List_Unorder:
    def __init__(self):
        self.List = []

    def add_list(self, val):
        self.List.append(val)

    def remove_list(self, val):
        self.List.remove(val)

    def search_list(self, val):
        if val in self.List:
            return True
        else:
            return False

    def is_empty(self):
        return self.List == []

    def size(self):
        return len(self.List)

    def append_list(self, val):
        self.List.append(val)

    def index_list(self, val):
        return self.List.index(val)

    def seart_list(self, val, pos):
        self.List.insert(pos, val)

    def pop(self):
        return self.List.pop()

    def popo(self, pos):
        return self.List.pop(pos)

