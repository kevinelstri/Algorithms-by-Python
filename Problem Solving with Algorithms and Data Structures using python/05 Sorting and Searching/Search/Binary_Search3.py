# coding:utf-8


def binary_search(string_list, item):
    if len(string_list) == 0:
        return False
    else:
        mid = len(string_list) / 2
        if string_list[mid] == item:
            return True
        elif string_list[mid] < item:
            print string_list[mid]
            return binary_search(string_list[mid + 1:], item)
        else:
            print string_list[mid]
            return binary_search(string_list[:mid], item)


string_list = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
item = 16
print binary_search(string_list, item)
