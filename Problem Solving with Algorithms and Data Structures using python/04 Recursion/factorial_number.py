# coding:utf-8


# The factorial of number
def factorial(number):
    try:
        if number == 1:
            return 1
        elif number >= 1:
            return number * factorial(number - 1)
    except Exception, e:
        print 'Please input a natural number:', e

number = -233
print factorial(number)
