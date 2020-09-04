def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
