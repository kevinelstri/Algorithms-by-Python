# coding:utf-8

'''
使用模块来实现单例模式
'''


class SingleTon(object):
    def __init__(self, val):
        self.val = val


single = SingleTon(3)
print single.val

a = single
b = single
print a.val, b.val  # 对象只有一个，a、b均为指向对象的指针
a.val = 33
print a.val, b.val  # 改变对象的值，指向对象的指针所在的值也都改变，同时，指针的值都相同
