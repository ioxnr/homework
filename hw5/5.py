with open('text_file.txt', 'w') as text_file:
    text_file.write('23 56 129 67 88 324 421 90')

with open('text_file.txt') as numbers_file:
    numbers = numbers_file.read()
    numbers = numbers.split()
    total = 0
    for i in numbers:
        total += int(i)
    print(total)
