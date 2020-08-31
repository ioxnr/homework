month = int(input('Введите номер месяца: '))

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

if month == 1 or month == 2 or month == 12:
    print(seasons_list[0])
    print(seasons_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(seasons_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict[4])
