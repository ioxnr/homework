with open('data.txt', 'w') as new_file:
    text = input('Введите данные: ')
    while text != '':
        new_file.writelines(text)
        text = input('Введите данные: ')
