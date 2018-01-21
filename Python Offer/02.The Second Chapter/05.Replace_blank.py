# coding:utf-8

import re


def replace_the_blank(s):
    s = s.replace(' ', '%20')
    return s


if __name__ == '__main__':
    s = 'The hello world'
    print replace_the_blank(s)
