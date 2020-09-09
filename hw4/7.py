def fact(n):
    result = 1

    if n <= 0:
        yield result

    for i in range(1, n + 1):
        result *= i
        yield result


n = int(input('Введите любое число: '))

for i in fact(n):
    print(i)
