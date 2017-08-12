# coding:utf-8

from stack_list_order import Stack


# using postfix to compute the result.
# this method only consider the interger.
def Postfix_compute(post_string):
    s = Stack()
    op = '+-*/'
    for p in post_string:
        if p not in op:
            s.push(int(p))
        else:
            second = s.pop()
            first = s.pop()
            re = op_math(first, second, p)
            s.push(re)
    return s.peek()


def op_math(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op1
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2

post_string = '456*+637+*+'
print Postfix_compute(post_string)
