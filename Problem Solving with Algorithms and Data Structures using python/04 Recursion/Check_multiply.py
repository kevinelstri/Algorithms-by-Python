# coding:utf-8


# fact(n) = n*(n-1)*(n-2)*...*1
def fact(n):
    while n == 1:
        return 1
    while n >= 2:
        return n * fact(n-1)

n = 10
print fact(n)
