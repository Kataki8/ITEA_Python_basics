import random
if __name__ == '__main__':
    a = 0
    number = random.randint(1, 100)
    while a != number:
        a = int(input('number : '))
        if a < number:
            print('small')
        elif a > number:
            print('big')
        else:
            print('guessed')
