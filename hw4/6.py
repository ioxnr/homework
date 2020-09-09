from itertools import count, cycle

a = int(input('Введите любое целое число: '))
new_list = []
for i in count(a):
    if i > 1000:
        break
    new_list.append(i)

print(new_list)

b = [3, 4, 5]
count = 0
for i in cycle(b):
    if count > 50:
        break
    print(i, end='')
    count += 1
