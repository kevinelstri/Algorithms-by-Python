# coding:utf-8


# 递归
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


num_list = [1, 2, 3, 4, 5]
print list_sum(num_list)

