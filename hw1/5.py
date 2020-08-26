earnings = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))

if earnings > costs:
    print('Фирма работает с прибылью')
    print('Рентабельность выручки составляет: ', earnings / costs)
    quantity = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника составляет: ', earnings / quantity)
elif earnings < costs:
    print('Фирма работает с убытками')
