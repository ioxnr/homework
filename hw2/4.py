n = input('Введите несколько значений через пробел: ').split()
n = [i for i in n]
for i in range(len(n)):
    if len(n[i]) > 10:
        new_string = n[i][:10]
        print(f'{i + 1}: {new_string}')
    else:
        print(f'{i + 1}: {n[i]}')
