# coding:utf-8


# Tree Traversals: preorder, inorder, postorder
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):  # 先序遍历
        print self.key
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):  # 中序遍历
        if self.left_child:
            self.left_child.inorder()
        print self.key
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):  # 后序遍历
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print self.key

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('e')
r.get_left_child().insert_left('c')
r.get_left_child().insert_right('f')
r.get_right_child().insert_left('g')
r.get_right_child().insert_right('h')

r.preorder()
print
r.inorder()
print
r.postorder()

