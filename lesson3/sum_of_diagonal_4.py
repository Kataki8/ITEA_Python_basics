if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal_sum = 0
    k = 0
    j = -2
    for i in matrix:
        print(i, "   " * k, i[k:j:])
        diagonal_sum = sum(i[k:j:])
        k += 1
        j += 1
    print('\nmatrix diagonal sum =', diagonal_sum)
