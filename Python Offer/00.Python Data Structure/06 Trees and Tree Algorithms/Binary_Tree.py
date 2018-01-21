# coding:utf-8

'''
二叉树
'''


class BinaryTree(object):
    # 二叉树的定义
    # __init__为构造器，就是二叉树的构成
    # self自动传入，代表实例对象本身
    def __init__(self, root):
        self.root = root  # 设置根节点
        self.left_child = None  # 设置左子树
        self.right_child = None  # 设置右子树

    # 以下为二叉树的功能，插入和查找数据
    def insert_left(self, new_nodel):
        if self.left_child is None:
            self.left_child = BinaryTree(new_nodel)
        else:
            t = BinaryTree(new_nodel)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_val(self):
        return self.root

    def set_root_val(self, val):
        self.root = val


if __name__ == '__main__':
    t = BinaryTree(2)
    t.insert_left(3)
    t.insert_right(4)
    print t.get_left_child()
    print t.get_right_child()
    print t.get_root_val()
