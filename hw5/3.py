with open('staff.txt') as my_file:
    total = 0
    quantity = 0
    for line in my_file.readlines():
        string = line.split()
        if float(string[1]) < 20000:
            print(string[0])
        total += float(string[1])
        quantity += 1
    print(f'Средняя величина дохода составляет {total / quantity}')
