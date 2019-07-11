# Найти сумму элементов матрицы


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in matrix:
        print(i)
    matrix_sum = sum(sum(i) for i in matrix)
    print('\nmatrix sum =', matrix_sum)
