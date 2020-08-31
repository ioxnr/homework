my_list = [7, 5, 3, 3, 2]
n = int(input('Введите новый элемент: '))

maximum = max(my_list)
if n > maximum:
    my_list.insert(0, n)
elif n in my_list:
    my_list.insert(my_list.index(n), n)
else:
    my_list.append(n)

print(my_list)
