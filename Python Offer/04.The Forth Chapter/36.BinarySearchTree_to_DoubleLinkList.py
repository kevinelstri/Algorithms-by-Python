# coding:utf-8

'''
二叉搜索树->双向链表
输入一颗二叉搜索树， 将该二叉搜索树转换成一个排序的双向链表
不能创建任何新的节点，只能调整树中节点的指针
'''


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    order = []

    # 中序遍历
    def inOrder(self, pRoot):
        if pRoot is None:
            return None
        self.inOrder(pRoot.left)
        self.order.append(pRoot.val)
        self.inOrder(pRoot.right)
        return self.order

    # 转换成双向链表
    def Convert(self, pRoot):
        if pRoot is None:
            return None

        # 转换左子树
        self.Convert(pRoot.left)
        left = pRoot.left
        if left:
            while left.right:
                left = left.right
            pRoot.left, left.right = left, pRoot

        # 转换右子树
        self.Convert(pRoot.right)
        right = pRoot.right
        if right:
            while right.left:
                right = right.left
            pRoot.right, right.left = right, pRoot

        # 转换根节点
        while pRoot.left:
            pRoot = pRoot.left
        return pRoot


if __name__ == '__main__':
    pRoot1 = BinaryTreeNode(10)
    pRoot2 = BinaryTreeNode(6)
    pRoot3 = BinaryTreeNode(14)
    pRoot4 = BinaryTreeNode(4)
    pRoot5 = BinaryTreeNode(8)
    pRoot6 = BinaryTreeNode(12)
    pRoot7 = BinaryTreeNode(16)

    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot3.left = pRoot6
    pRoot3.right = pRoot7

    s = Solution()
    root = s.Convert(pRoot1)
    print root.right.val
