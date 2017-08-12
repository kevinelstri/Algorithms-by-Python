# coding:utf-8


# Sequential search
def Seq(string_list, item):
    pos = 0
    result = False
    while pos < len(string_list):
        if string_list[pos] == item:
            result = True
        pos += 1
    return result


string_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
item = 0
print Seq(string_list, item)
