# coding:utf-8

#  Implement the remaining simple arithmetic operators
# (__sub__, __mul__, and __truediv__)


def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_m
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        number = gcd(new_num, new_den)
        return Fraction(new_num / number, new_den / number)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        number = gcd(new_num, new_den)
        return Fraction(new_num / number, new_den / number)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        number = gcd(new_num, new_den)
        print number
        return Fraction(new_num / number, new_den / number)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        number = gcd(new_num, new_den) + 0.0
        print number
        return Fraction(new_num / number, new_den / number)

    def show(self):
        return self.num + '/' + self.den


x = Fraction(1, 2)
y = Fraction(3, 4)
print x.__add__(y)
print x.__sub__(y)
print x.__mul__(y)
print x.__truediv__(y)

