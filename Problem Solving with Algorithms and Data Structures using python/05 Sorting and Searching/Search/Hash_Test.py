# coding:utf-8


def Hash_Test(string_list, item):
    if len(string_list) == 0:
        return False
    else:
        if string_list.index[item] is not Exception:
            return True
        return False


string_list = [45, 35, 6, 66, 55, 43, 35, 5, 7, 65, 79, 8, 3, 4, 2, 42]
item = 8
print Hash_Test(string_list, item)
