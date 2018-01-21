# coding:utf-8

'''
使用__new__来实现单例模式
将一个类的实例绑定到类变量_instance上，
如果cls._instance为None，说明该类还没有实例化过，实例化该类，并返回
如果cls._instance不为None，直接返回cls._instance
'''


class SingleTon(object):
    '''
    任何以单下划线_开头的名字都应该是内部实现
    '''
    _instance = {}  # 内部属性

    '''
    __new__() :始终是类的静态方法，即使没有加静态方法装饰器
    cls：表示当前正在实例化的类
    args:表示位置参数
    kwargs:表示命名参数
    '''

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
            print cls._instance  # 类的实例
        return cls._instance[cls]


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val

    def obj_fun(self):
        print self.val, 'obj_fun'

    @staticmethod
    def static_fun():
        print 'staticmethod'

    @classmethod
    def class_fun(cls):
        print cls.class_val, 'classmethod'


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)

    print '-----------------------'
    print a
    print b
    print a == b  # 判断两个对象是否相等
    print a is b  # 判断两个对象是否相同，单例模式下对象都是一样的
    print id(a)  # 53472952 单例模式下对象的编号
    print id(b)  # 53472952 单例模式下对象的编号的相同的

    # 实例类型
    print type(a)  # 对象的类型，MyClass作为对象的类型，SingleTon类是单例模式的定义
    print type(b)  #

    # 实例方法
    a.obj_fun()  # 实例对象的方法 2 obj_fun
    b.obj_fun()  # 实例对象的方法 2 obj_fun

    # 类方法
    MyClass.class_fun()  # 22 classmethod 单例模式下类对象是一样的
    a.class_fun()  # 22 classmethod
    b.class_fun()  # 22 classmethod

    # 静态方法
    MyClass.static_fun()  # staticmethod
    a.static_fun()  # staticmethod
    b.static_fun()  # staticmethod

    # 类变量
    a.class_val = 33
    MyClass.class_fun()  # 22 classmethod
    a.class_fun()  # 22 classmethod
    b.class_fun()  # 22 classmethod
    print MyClass.class_val  # 22
    print a.class_val  # 33
    print b.class_val  # 33

    # 实例变量
    print a.val  # 2
    print b.val  # 2
