# coding:utf-8

from stack_list_order import Stack

# Decimal to Octal:start with a '0'
def DecimaltoOctal(number):
    s = Stack()
    o = '0'
    if number == 0:
        o += '0'
    else:
        while number != 0:
            s.push(number%8)
            number /=8
        while not s.is_empty():
            o += str(s.peek())
            s.pop()
    return o

number = 10
print DecimaltoOctal(number)
