total = 0
n = 1


def my_sum(*args):
    numbers = ' '.join(args)
    numbers = numbers.split(' ')
    global total
    for i in numbers:
        if i.startswith('\\'):
            global n
            n = 0
            return 'Введен спецсимвол\n' f'Cумма чисел равна {total}'
        else:
            total = total + int(i)
    return total


while n != 0:
    print(my_sum(input('Введите числа через пробел: ')))
