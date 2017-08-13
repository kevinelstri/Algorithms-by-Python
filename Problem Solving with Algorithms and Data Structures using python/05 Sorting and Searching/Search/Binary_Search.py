# coding:utf-8


# Binary Search
def BinSearch(string_list, item):
    first = 0
    last = len(string_list) - 1
    result = False
    while first <= last and not result:
        mid = (first + last) / 2
        if string_list[mid] == item:
            result = True
        elif string_list[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return result


string_list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
item = 4
print BinSearch(string_list, item)
