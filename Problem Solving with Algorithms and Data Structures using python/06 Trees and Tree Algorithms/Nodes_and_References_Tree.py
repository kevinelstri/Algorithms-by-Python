# coding:utf-8


# Nodes and References

# define a class that has sttributes for the root value,
# as well as the left and right subtrees.

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
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

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
print r.get_right_child()
print r.get_left_child()
print r.get_root_val()
print r

# Exercise
x = BinaryTree('a')
x.insert_left('b')
x.insert_right('c')
x.get_left_child().insert_right('d')
x.get_right_child().insert_right('f')
x.get_right_child().insert_left('e')
print x


