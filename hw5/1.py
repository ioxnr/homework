while True:
    with open('data.txt', 'a+') as new_file:
        text = input('Введите данные: ')
        if text == '':
            break
        new_file.write(text + '\n')
