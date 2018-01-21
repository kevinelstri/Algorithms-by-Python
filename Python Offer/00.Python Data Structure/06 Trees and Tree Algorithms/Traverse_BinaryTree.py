# coding:utf-8

'''
遍历二叉树：
前序遍历，中序遍历，后序遍历，层次遍历
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 前序遍历：根节点->左节点->右节点
    def FirstTraverse(self, pRoot):
        if pRoot is None:
            return
        print pRoot.val,
        self.FirstTraverse(pRoot.left)
        self.FirstTraverse(pRoot.right)

    # 前序遍历的反向表示方式：根节点->右节点->左节点
    def Reverse_FirstTraverse(self, pRoot):
        if pRoot is None:
            return
        print pRoot.val,
        self.Reverse_FirstTraverse(pRoot.right)
        self.Reverse_FirstTraverse(pRoot.left)

    # 中序遍历：左节点->根节点->右节点
    def MiddleTraverse(self, pRoot):
        if pRoot is None:
            return
        self.MiddleTraverse(pRoot.left)
        print pRoot.val,
        self.MiddleTraverse(pRoot.right)

    # 中序遍历的反向表示方式：右节点->根节点->左节点
    def Reverse_MiddleTraverse(self, pRoot):
        if pRoot is None:
            return
        self.Reverse_MiddleTraverse(pRoot.right)
        print pRoot.val,
        self.Reverse_MiddleTraverse(pRoot.left)

    # 后序遍历：左节点->右节点->跟节点
    def LastTraverse(self, pRoot):
        if pRoot is None:
            return
        self.LastTraverse(pRoot.left)
        self.LastTraverse(pRoot.right)
        print pRoot.val,

    # 后序遍历的反向表示方式：右节点->左节点->根节点
    def Reverse_LastTraverse(self, pRoot):
        if pRoot is None:
            return
        self.Reverse_LastTraverse(pRoot.right)
        self.Reverse_LastTraverse(pRoot.left)
        print pRoot.val,

    # 层次遍历
    def LevelTraverse(self, pRoot):
        if pRoot is None:
            return
        if pRoot.left is not None:
            print pRoot.left.val,
        if pRoot.right is not None:
            print pRoot.right.val,
        self.LevelTraverse(pRoot.left)
        self.LevelTraverse(pRoot.right)


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(5)
    pRoot3 = BinaryTreeNode(12)
    pRoot4 = BinaryTreeNode(4)
    pRoot5 = BinaryTreeNode(7)
    pRoot6 = BinaryTreeNode(13)
    pRoot7 = BinaryTreeNode(14)

    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot3.left = pRoot6
    pRoot3.right = pRoot7

    s = Solution()
    print '前序遍历   ：', s.FirstTraverse(pRoot1)  # ok
    print '反向前序遍历：', s.Reverse_FirstTraverse(pRoot1)  # ok
    print '中序遍历   ：', s.MiddleTraverse(pRoot1)  # ok
    print '反向中序遍历：', s.Reverse_MiddleTraverse(pRoot1)  # ok
    print '后序遍历   ：', s.LastTraverse(pRoot1)  # ok
    print '反向后序遍历：', s.Reverse_LastTraverse(pRoot1)  # ok
    print '层次遍历   ：', pRoot1.val,
    print s.LevelTraverse(pRoot1)  # ok

