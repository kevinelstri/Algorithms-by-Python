# coding:utf-8

from stack_list_order import Stack


# infix,prefix,postfix: 内缀，前缀，后缀
# 1.create an empty stack called s for keeping operators. create an empty list for output.
# 2.convert the input infix string to a list by using the string method split.
# 3.scan the token list from left to right.
#   if the token is an operand,append it to the end of the output list
#   if the token is a left parenthesis,push it on the op_stack
#   if the token is a right parenthesis, pop the op_stack until the corresponding left
#      parenthesis is removed. Append each operator to the end of the output list.
#   if the token is an operator,*,/,+,or -, push it on the op_stack.However, first remove
#      any operators already on the op_stack that have higher or equal precedence and qppend
#      them to the output list.
def Postfix(infix_string):
    s = Stack()
    # post = ''
    op = '+-*/()'
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 4}
    op_list = []
    for p in infix_string:
        if p not in op:
            op_list.append(p)
        elif s.peek() == None:
            s.push(p)
        elif op_dict[s.peek()] != 3 and op_dict[s.peek()] >= op_dict[p]:
            op_list.append(s.pop())
            s.push(p)
        elif op_dict[p] == 4:
            while op_dict[s.peek()] != 3:
                op_list.append(s.pop())
            else:
                s.pop()
        else:
            s.push(p)
    while s.peek() != None:
        op_list.append(s.pop())
    return op_list


infix_string = '(a+(b*c+7))*c*d'
print Postfix(infix_string)
