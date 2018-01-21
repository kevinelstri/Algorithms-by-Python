# coding:utf-8

'''
第K大节点：
给定一颗二叉搜索树，找出其中第K大节点
'''

'''
实质上：二叉搜索树的中序遍历
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    treeNode = []  # 全局成员变量

    def inOrder(self, pRoot):
        if pRoot is None:
            return None
        self.inOrder(pRoot.left)
        self.treeNode.append(pRoot.val)
        self.inOrder(pRoot.right)

    def FindKNode(self, pRoot, k):
        if pRoot is None or k <= 0:
            return
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]


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

    s = Solution()
    print s.FindKNode(pRoot1, 3)
