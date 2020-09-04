def my_func(x, y):
    return x ** y


print(my_func(int(input('Введите положительное число x: ')), int(input('Введите отрицательное число y: '))))


def my_func(x, y):  # 2 cпособ
    y = abs(y)
    i = 1
    while y > 0:
        i = i * x
        y = y - 1
    return i


print(my_func(int(input('Введите положительное число x: ')), int(input('Введите отрицательное число y: '))))
