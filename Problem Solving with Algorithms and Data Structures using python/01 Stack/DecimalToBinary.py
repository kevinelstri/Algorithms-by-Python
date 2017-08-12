# coding:utf-8

from stack_list_order import Stack


# Decimal to Binary
def DecimaltoBinary(number):
    s = Stack()
    b = ''
    if number == 0:
        b += str(0)
    else:
        while number != 0:
            s.push(number % 2)
            number /= 2

        while s.peek() != None:
            b += str(s.peek())
            s.pop()
    return b

number = 64
b = DecimaltoBinary(number)
print b
