# coding:utf-8


# insert sort: insert the number one by one
def insertSort(num_list):
    leng = len(num_list)
    L = 1
    while L < leng:
        index = L
        while index >= 1 and num_list[index] < num_list[index - 1]:
            temp = num_list[index]
            num_list[index] = num_list[index - 1]
            num_list[index - 1] = temp
            index -= 1
        L += 1
    return num_list


if __name__ == '__main__':
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print insertSort(num_list)
