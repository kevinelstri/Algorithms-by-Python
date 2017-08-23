# coding:utf-8


# shell sort
def shellSort(num_list):
    L = len(num_list)
    shell_count = len(num_list)/2
    while shell_count > 0:
        for i in range(0, L, shell_count):
            for j in range(i + shell_count, L, shell_count):
                if num_list[i] > num_list[j]:
                    temp = num_list[i]
                    num_list[i] = num_list[j]
                    num_list[j] = temp
        print num_list
        shell_count /= 2
    print


if __name__ == '__main__':
    num_list1 = [3, 7, 5, 8, 9, 12, 19, 16, 20, 17]
    num_list2 = [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]
    num_list3 = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
    num_list4 = [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]
    shellSort(num_list1)
    shellSort(num_list2)
    shellSort(num_list3)
    shellSort(num_list4)
