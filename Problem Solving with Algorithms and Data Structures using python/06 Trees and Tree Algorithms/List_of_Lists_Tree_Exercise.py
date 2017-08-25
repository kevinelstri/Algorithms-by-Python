# coding:utf-8


# Exercise
def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val


def get_left_val(root):
    return root[1]


def get_right_val(root):
    return root[2]

# Exercise1
x = binary_tree('a')
insert_left(x, 'b')
insert_right(x, 'c')
insert_right(get_right_val(x), 'd')
insert_left(get_right_val(get_right_val(x)), 'e')
print x

# Exercise2
x = binary_tree('a')
insert_left(x, 'b')
insert_right(x, 'c')
y = get_left_val(x)
insert_right(y, 'd')
z = get_right_val(x)
insert_right(z, 'f')
insert_left(z, 'e')
print x

