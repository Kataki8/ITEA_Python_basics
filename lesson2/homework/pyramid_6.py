def draw_pyramid(x):
    for i in range(1, x + 1):
        s = " " * (x-i) + "^" * ((i * 2) - 1)
        print(s)


if __name__ == "__main__":
    a = int(input('input height '))
    draw_pyramid(a)
