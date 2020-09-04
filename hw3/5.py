total = 0
n = 1


def my_sum(*args):
    numbers = ' '.join(args)
    numbers = numbers.split(' ')
    global total
    for i in numbers:
        if i.isdigit():
            total = total + int(i)
        else:
            global n
            n = 0
            return 'Введен спецсимвол\n' f'Cумма чисел равна {total}'
    return total


while n != 0:
    print(my_sum(input('Введите числа через пробел: ')))
