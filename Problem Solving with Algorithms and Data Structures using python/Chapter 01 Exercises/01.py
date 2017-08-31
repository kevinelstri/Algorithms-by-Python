# coding:utf-8

# Question: Implement the simple methods get_num and
# get_den that will return the numerator and denominator of a fraction.
# 返回一个分数的分子和分母


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

x = Fraction(1, 2)
print x.get_den()
print x.get_num()



