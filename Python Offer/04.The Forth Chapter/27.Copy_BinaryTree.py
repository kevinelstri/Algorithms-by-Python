# coding:utf-8

'''
二叉树的镜像
输入一颗二叉树，输出该树的镜像
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __delleft__(self):
        self.left = None

    def __delright__(self):
        self.right = None


# 二叉树递归算法，不需要写递归结束标记，会自动到达结束标记
class Solution(object):
    def CopyTree(self, pRoot):
        if pRoot is None:
            return None
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.CopyTree(pRoot.left)
        self.CopyTree(pRoot.right)
        return pRoot


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(11)
    pRoot3 = BinaryTreeNode(12)
    pRoot4 = BinaryTreeNode(13)
    pRoot5 = BinaryTreeNode(14)

    pRoot1.left = pRoot2  # 11
    pRoot1.right = pRoot3  # 12
    pRoot2.left = pRoot4  # 13
    pRoot4.right = pRoot5  # 14

    s = Solution()
    tree = s.CopyTree(pRoot1)
    print tree.val
    print tree.left.val
    print tree.right.val
    print tree.right.right.val
