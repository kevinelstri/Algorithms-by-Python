# coding:utf-8

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

    def show(self):
        print self.num, '/', self.den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def add(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den

        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num


x = Fraction(6, 8)
y = Fraction(6, 8)
print x
print x.add(y)
# print x == y
