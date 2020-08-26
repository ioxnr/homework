number = int(input('Введите любое число: '))
maximum = 0
while number > 0:
    a = number % 10
    if a > maximum:
        maximum = a
    number = number // 10

print("Самое большая цифра в числе: ", maximum)
