# coding:utf-8

'''
序列化二叉树
实现两个函数，分别用来序列化和反序列化二叉树
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 序列化二叉树
    def SequenceTree(self, pRoot):
        if pRoot is None:
            print '$',
        if pRoot is not None:
            print pRoot.val,
            self.SequenceTree(pRoot.left)
            self.SequenceTree(pRoot.right)



if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(8)
    pRoot2 = BinaryTreeNode(8)
    pRoot3 = BinaryTreeNode(7)
    pRoot4 = BinaryTreeNode(9)
    pRoot5 = BinaryTreeNode(2)
    pRoot6 = BinaryTreeNode(4)
    pRoot7 = BinaryTreeNode(7)

    # first
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    # second
    pRoot8 = BinaryTreeNode(1)
    pRoot9 = BinaryTreeNode(2)
    pRoot10 = BinaryTreeNode(3)
    pRoot11 = BinaryTreeNode(4)
    pRoot12 = BinaryTreeNode(5)
    pRoot13 = BinaryTreeNode(6)

    pRoot8.left = pRoot9
    pRoot8.right = pRoot10
    pRoot9.left = pRoot11
    pRoot10.left = pRoot12
    pRoot10.right = pRoot13

    s = Solution()
    s.SequenceTree(pRoot1)
    print
    s.SequenceTree(pRoot8)
