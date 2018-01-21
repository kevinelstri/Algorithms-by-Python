# coding:utf-8

'''
礼物的最大价值
'''


def maxValue(matrix, i, j, value):
    row = len(matrix)
    col = len(matrix[0])
    while i < row-1 and j < col-1:
        if matrix[i + 1][j] >= matrix[i][j + 1]:
            value += matrix[i + 1][j]
            i += 1
        else:
            value += matrix[i][j + 1]
            j += 1
    while i == row-1 and j < col-1:
        value += matrix[i][j + 1]
        j += 1
    while i < row-1 and j == col:
        value += matrix[i + 1][j]
        i += 1
    # value = maxValue(matrix, i, j, value)
    return value


if __name__ == '__main__':
    matrix = [[1, 10, 3, 8],
              [12, 2, 9, 6],
              [5, 7, 4, 11],
              [3, 7, 16, 5]]
    value = 0
    value += matrix[0][0]
    i, j = 0, 0
    print maxValue(matrix, i, j, value)
