counter = int(input('Введите количество элементов списка: '))
n = []
i = 0

while i < counter:
    n.append(input('Введите любое значение: '))
    i += 1

element = 0
new_list = []

while len(n) > 1:
    new_list.append(n[element + 1])
    new_list.append(n[element])
    del n[element + 1]
    del n[element]

if len(n) > 0:
    new_list.append(n[0])

print(new_list)
