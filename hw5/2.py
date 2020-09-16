with open('new_text.txt') as my_file:
    count = 0
    for line in my_file.readlines():
        strings = line.split()
        words = len(strings)
        count += 1
        print(f'Количество слов в строке {count} равно {words}')
    print(f'Количество строк равно {count}')
