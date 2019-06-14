# Возвести число в степень с помощью цикла
def calculate_degree(x, y):
    z = x
    for i in range(y - 1):
        z = z * x
    return z


if __name__ == "__main__":
    a = int(input('number : '))
    b = int(input('degree : '))
    print(calculate_degree(a, b))
