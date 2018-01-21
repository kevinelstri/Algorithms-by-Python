# coding:utf-8

class Btree(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def insertleft(self, value):
        self.left = Btree(value)
        return self.left

    def insertright(self, value):
        self.right = Btree(value)
        return self.right

    def show(self):
        print self.data


