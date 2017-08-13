# coding:utf-8


# order Sequential search
def order_seq(string_list, item):
    pos = 0
    result = False
    while pos < len(string_list):
        if string_list[pos] == item:
            result = True
            break
        elif string_list[pos] > item:
            break
        pos += 1
    return result


string_list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
item = 3
print order_seq(string_list, item)
