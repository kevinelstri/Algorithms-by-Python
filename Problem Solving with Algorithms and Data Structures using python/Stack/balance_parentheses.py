# coding:utf-8

# This is a using of stack,using stack to solve real computer science problems.
# using stack to judge the parenthese is balance or not.
from stack_list_order import Stack


# First, we define the "(" as 0 and the ")" as 1
# (()((())()))
# (()()(()
# P = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0]
# s = Stack()
# for p in P:
#     if p != 0:
#         s.push(p)
#     else:
#         s.pop()
# print s.size()
# print s.is_empty()


# 注意：这里有三种情况，1：右括号大于左括号，2：左括号右括号相等，3：左括号大于右括号
# def par_checker(symbol_string):
#     s = Stack()
#     for i in range(len(symbol_string)):
#         if symbol_string[i] != ')':
#             s.push(symbol_string[i])
#         else:
#             if s.is_empty():
#                 return False
#             else:
#                 s.pop()
#     return s.is_empty()
#
# print par_checker('()()))))')


def gen_sym_cheker(symbol_string):
    s = Stack()
    for i in range(len(symbol_string)):
        if symbol_string[i] not in '([{})]':
            return False
        if symbol_string[i] in '([{':
            s.push(symbol_string[i])
        else:
            if s.is_empty():
                return False
            else:
                if not match(s.peek(), symbol_string[i]):
                    return False
                s.pop()
    return s.is_empty()


def match(x, y):  # 括号匹配函数
    X = '([{'
    Y = ')]}'
    return X.index(x) == Y.index(y)


symbol_string = '{{[{]}}'
print gen_sym_cheker(symbol_string)
