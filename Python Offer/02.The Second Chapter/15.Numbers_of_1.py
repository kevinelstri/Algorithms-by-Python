# coding:utf-8

'''
输入一个整数，判断整数所对应的二进制中1的个数
'''


# 使用整数与其小1的整数进行“与”运算，可以不断将整数二进制逆向按位增加0
def numbers(num):
    count = 0
    while num != 0:
        num = num & (num - 1)
        count += 1
    return count


if __name__ == '__main__':
    print numbers(8)
    print numbers(0)
    print numbers(99999999999999999999999999999999999999999999999999999999999999999999)

