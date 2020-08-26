a = int(input('Результат в первый день (км): '))
b = int(input('Спортсмен должен пробежать не менее: '))
i = 1

while a < b:
    a = a + a / 10
    i = i + 1

print(i)
