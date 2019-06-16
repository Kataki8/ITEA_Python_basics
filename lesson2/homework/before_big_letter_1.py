# Выводить буквы строки, до первой заглавной
if __name__ == "__main__":
    line = str(input())
    for i in line:
        if i.isupper:
            print(i)
        else:
            break
