translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
russian = []
with open('numbers.txt') as new_file:
    for line in new_file.readlines():
        line = line.split()
        if line[0] in translator:
            russian.append(line[0] + ' - ' + translator[line[0]])

with open('new_numbers.txt', 'w') as translation_file:
    for i in russian:
        translation_file.write(i + '\n')
