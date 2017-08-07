# coding:utf-8

from stack_list_order import Stack


# implement the reverse string
def Reverse(r_string):
    s = Stack()
    Reverse_string = ''
    for r in r_string:
        s.push(r)
    while not s.is_empty():
        Reverse_string += s.pop()
    return Reverse_string


r_string = '123hwehfdweif'
print Reverse(r_string)
