# Проверить является ли введенное число простым.
# Число считается простым если оно не делится нацело
# на все числа до квадратного корня этого числа
import math


def is_prime(x):
    for i in range(x-1, int(round(math.sqrt(x))), -1):
        if not x % i:
            return False
    return True


if __name__ == '__main__':
    a = int(input('number : '))
    if is_prime(a):
        print(a, "is prime")
    else:
        print(a, "is not prime")
