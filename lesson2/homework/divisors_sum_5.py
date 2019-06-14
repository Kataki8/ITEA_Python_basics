# Вывести сумму всех делителей заданного числа
def sum_of_divisors(x):
    divisors_sum = 0
    for i in range(1, x):
        if not x % i:
            divisors_sum += i
    return divisors_sum


if __name__ == "__main__":
    a = int(input('number : '))
    print(sum_of_divisors(a))
