def fact(n):
    result = 1

    if n <= 0:
        yield result

    for x in range(1, n + 1):
        result *= x
        yield result


n = int(input('Введите любое число: '))

for i in fact(n):
    print(i)
