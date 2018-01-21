# coding:utf-8

'''
使用先序遍历和中序遍历 重建二叉树
'''
from collections import deque


class TreeNode(object):
    # __init__构造器，二叉树结构定义
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 继承自TreeNode树的结构
class Tree(TreeNode):
    def __init__(self):
        self.root = None

    # 广度优先搜索遍历，层次遍历
    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    # 先序遍历
    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)

        traversal(self.root)
        return ret

    # 中序遍历
    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    # 后序遍历
    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret


# 重建二叉树
def construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1 + len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root


if __name__ == '__main__':
    t = Tree()
    preorder, inorder = [1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_tree(preorder, inorder)
    t.root = root
    print t.bfs()
    print t.pre_traversal()
    print t.in_traversal()
    print t.post_traversal()
