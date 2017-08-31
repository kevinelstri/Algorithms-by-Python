# coding:utf-8

# In many ways it would be better if all fractions were maintained in lowest terms right
# from the start. Modify the constructor for the Fraction class so that GCD is used to
# reduce fractions immediately. Notice that this means the __add__ function no longer
# needs to reduce. Make the necessary modifications


def gcd(num, den):
    while num % den != 0:
        old_num = num
        old_den = den

        num = old_num
        den = old_num % old_den
    return den


class Fraction:
    def __init__(self, top, bottem):
        self.num = top
        self.den = bottem

    def show(self):
        return self.num + '/' + self.den

    # 将一个对象转换成字符串
    # 默认情况下，实现一个方法来返回实例地址字符串
    # 重写__str__()方法，来实现字符串形式的输出
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def add(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.num * other.num

        number = gcd(new_num, new_den)
        return Fraction(new_num/number, new_den/number)

x = Fraction(7, 9)
y = Fraction(3, 6)
print x.add(y)


