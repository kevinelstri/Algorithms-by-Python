# coding:utf-8


# Reverse a list by recursive
def Reverse_list(string_list):
    if len(string_list) == 1:
        return string_list[0]
    else:
        return string_list[-1] + Reverse_list(string_list[:-1])

string_list = '1738323839289382938923892'
print Reverse_list(string_list)
