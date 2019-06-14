# Выводить буквы строки, до первой заглавной
if __name__ == "__main__":
    print('input string')
    line = str(input())
    for i in line:
        if not i.isupper():
            print(i, end='')
        else:
            break
