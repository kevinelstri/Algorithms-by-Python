# coding:utf-8

'''
二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
'''


def find_integer_leftdown(matrix, num):
    '''
    从矩阵左下角开始比较
    :param matrix: [[]]
    :param num: int
    :return: bool
    '''
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])  # 行,列
    row, col = rows - 1, 0  #
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False


def find_integer_rightupper(matrix, num):
    '''
    从矩阵右上角开始比较大小
    :param matrix:
    :param num:
    :return:
    '''
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            col -= 1
        else:
            row += 1
    return False


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    num = 20
    print find_integer_leftdown(matrix, num)
    print find_integer_rightupper(matrix, num)
