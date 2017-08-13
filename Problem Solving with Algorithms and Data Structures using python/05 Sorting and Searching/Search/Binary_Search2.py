# coding:utf-8


def binary_search(string_list, item):
    if len(string_list) == 0:
        return False
    else:
        mid = len(string_list)/2
        if string_list[mid] == item:
            return True
        else:
            if string_list[mid] < item:
                print string_list[mid+1:]
                return binary_search(string_list[mid+1:], item)
            else:
                print string_list[:mid]
                return binary_search(string_list[:mid], item)

string_list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
item = 3
print binary_search(string_list, item)
