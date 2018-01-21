# coding:utf-8

'''
二叉排序树
'''


# 二叉排序树节点结构
class BSTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree(object):
    stack = []

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # 二叉排序树创建（插入）
    def insert(self, val):
        p = self.root
        if self.root is None:
            self.root = BSTreeNode(val)
            return
        while p is not None:
            if p.data > val:
                if p.left is None:
                    p.left = BSTreeNode(val)
                    return
                p = p.left
            elif p.data < val:
                if p.right is None:
                    p.right = BSTreeNode(val)
                    return
                p = p.right
            else:
                p.data = val
                return

    # 查找
    def search(self, val):
        p = self.root
        while p:
            if p.data == val:
                return True
            elif p.data > val:
                p = p.left
            elif p.data < val:
                p = p.right
        return False

    # 中序遍历
    def intraverse(self, pRoot):
        if pRoot is None:
            return None
        self.intraverse(pRoot.left)
        print pRoot.data
        self.intraverse(pRoot.right)


if __name__ == '__main__':
    list = [26, 17, 41, 14, 21, 30, 47]
    bs = BinarySortTree()
    for i in range(len(list)):
        bs.insert(list[i])
    # print bs.root.data
    # print bs.root.left.data
    # print bs.root.left.left.data
    # print bs.root.left.right.data
    # print bs.root.right.data
    # print bs.root.right.left.data
    # print bs.root.right.right.data
    # print bs.search(31)

    bs.intraverse(bs.root)
