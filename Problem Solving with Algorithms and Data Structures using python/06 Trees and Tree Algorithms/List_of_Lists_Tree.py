# coding:utf-8


# List of Lists Representation

# build tree by a list of lists,store the value of the root node as the first
# element of the list. The second element of the list will itself be a list that
# represents the left subtree. The third element of the list will be another list
# that represents the right subtree.

# list_of_tree_1 = ['a', ['b', [], []], ['c', [], []]]
# print list_of_tree_1
# print 'left subtree:', list_of_tree_1[1]
# print 'right subtree:', list_of_tree_1[2]
# print '------------------------------------------------'
#
# list_of_tree_2 = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], ['g', [], []]]]
# print list_of_tree_2
# print list_of_tree_2[1][1]
# print list_of_tree_2[1][2]
# print list_of_tree_2[2][1]
# print list_of_tree_2[2][2]
# print '------------------------------------------------'


def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])  # 在左子树的基础上插入
    else:
        root.insert(1, [new_branch, [], []])  # 直接从根节点插入
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])  # 在右子树的基础上插入
    else:
        root.insert(2, [new_branch, [], []])  # 直接从根节点插入
    return root


def get_root_val(root):  # 获取根节点的值
    return root[0]


def set_root_val(root, new_val):  # 设置根节点的值
    root[0] = new_val


def get_left_child(root):  # 返回左孩子
    return root[1]


def get_right_child(root):  # 返回右孩子
    return root[2]


r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print r
l = get_right_child(r)
print l

set_root_val(l, 9)
print r
insert_right(l, 11)
print r
