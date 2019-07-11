# Найти сумму верхней диагонали матрицы


if __name__ == '__main__':
    matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    matrix_sum = 0
    k = 0
    for i in matrix:
        print(i, "   " * k, i[k:])
        matrix_sum += sum(i[k:])
        k += 1
    print('\nmatrix top diagonal sum =', matrix_sum)
