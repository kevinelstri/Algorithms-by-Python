# coding:utf-8


# select sort:select the max number and change with the last one
def selectSort(num_list):
    leng = len(num_list)
    L = -1
    while L > -leng:
        max_num = max(num_list[:L])  # 选择list中最大的数
        x = num_list.index(max_num)  # 最大数所在的list中的位置
        if num_list[x] > num_list[L]:
            temp = num_list[x]
            num_list[x] = num_list[L]
            num_list[L] = temp
        L -= 1
    print num_list

if __name__ == '__main__':
    num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectSort(num_list)
