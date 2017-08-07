# coding:utf-8

from stack_list_order import Stack


# Decimal to Hex: start with '0x'
def DecimaltoHex(number):
    s = Stack()
    h = '0x'
    H = 'ABCDEF'
    if number == 0:
        h += '0'
    else:
        while number != 0:
            s.push(number % 16)
            number /= 16
        while not s.is_empty():
            if s.peek() >= 10:
                h += str(H[s.peek() - 10])
            else:
                h += str(s.peek())
            s.pop()
    return h


number = 0
print DecimaltoHex(number)
