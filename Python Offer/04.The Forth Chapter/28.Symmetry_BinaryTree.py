# coding:utf-8

'''
对称二叉树
实现一个函数，用来判断一个二叉树是不是对称的
如果一颗二叉树和它的镜像是一样的，就是对称的
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetryBonaryTree(self, pRoot):
        if pRoot is None:
            return False
        pRoot.right, pRoot.left = pRoot.left, pRoot.right
        self.isSymmetryBonaryTree(pRoot.left)
        self.isSymmetryBonaryTree(pRoot.right)
        return pRoot


if __name__ == '__main__':
    # The first Binary Tree
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(12)
    pRoot3 = BinaryTreeNode(12)

    pRoot1.left = pRoot2
    pRoot1.right = pRoot3

    # The second Binary Tree
    pRoot4 = BinaryTreeNode(13)
    pRoot5 = BinaryTreeNode(14)
    pRoot6 = BinaryTreeNode(14)
    pRoot7 = BinaryTreeNode(16)
    pRoot8 = BinaryTreeNode(17)
    pRoot9 = BinaryTreeNode(17)
    pRoot10 = BinaryTreeNode(16)

    pRoot4.left = pRoot5
    pRoot4.right = pRoot6
    pRoot5.left = pRoot7
    pRoot5.right = pRoot8
    pRoot6.left = pRoot9
    pRoot6.right = pRoot10

    # The third Binary Tree
    pRootx1 = BinaryTreeNode(100)
    pRootx2 = BinaryTreeNode(102)
    pRootx3 = BinaryTreeNode(103)

    pRootx1.left = pRootx2
    pRootx1.right = pRootx3

    s = Solution()
    pRootCopy1 = s.isSymmetryBonaryTree(pRoot1)
    print pRootCopy1 == pRoot1

    pRootCopy4 = s.isSymmetryBonaryTree(pRoot4)
    print pRootCopy4 == pRoot4

    pRootCopyx1 = s.isSymmetryBonaryTree(pRootx1)
    print pRootCopyx1 == pRootx1
