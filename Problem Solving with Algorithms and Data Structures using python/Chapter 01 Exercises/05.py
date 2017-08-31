# coding:utf-8


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        return self.num + '/' + self.den

    def __str__(self):
        if int(self.num)*10 == self.num*10 and int(self.den)*10 == self.den*10:
            return str(self.num) + '/' + str(self.den)
        else:
            raise ValueError

x = Fraction(1.2, 2)
print x
