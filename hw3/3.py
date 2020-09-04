def my_func(a, b, c):
    my_list = [a, b, c]
    new_list = sorted(my_list)
    return new_list[1] + new_list[2]


print(my_func(int(input('Введите число a: ')), int(input('Введите число b: ')), int(input('Введите число c: '))))
