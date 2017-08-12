# coding:utf-8


# Convert Interger to String in any base
# 十进制，二进制，八进制，十六进制等所有进制都可以转换
def Convert(n, base):
    M = 'ABCDEF'
    if n < base and (base != 16):
        return str(n)
    elif n < base and (base == 16):
        if n >= 10:
            return M[n - 10]
        else:
            return str(n)
    else:
        return Convert(n / base, base) + str(n % base)


n = 8
base = 8
print Convert(n, base)
