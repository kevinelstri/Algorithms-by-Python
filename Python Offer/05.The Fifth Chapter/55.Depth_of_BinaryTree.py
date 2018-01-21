# coding:utf-8

'''
二叉树的深度
输入一颗二叉树的根节点，求该树根的深度
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def TreeDepth(self, pRoot):

        if pRoot is None:
            return 0

        nleft = self.TreeDepth(pRoot.left)
        nright = self.TreeDepth(pRoot.right)
        return max(nleft, nright)+1


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(5)
    pRoot3 = BinaryTreeNode(12)
    pRoot4 = BinaryTreeNode(4)
    pRoot5 = BinaryTreeNode(7)

    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5

    s = Solution()
    print s.TreeDepth(pRoot1)
