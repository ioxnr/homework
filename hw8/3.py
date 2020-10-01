class OnlyNumbersException(Exception):

    def __str__(self):
        return 'Недопустимое значение, введите число'


numbers = []


def append_numbers(numbers):
    value = input('Введите число: ')
    try:
        numbers.append(int(value))
    except ValueError:
        raise OnlyNumbersException


while True:
    try:
        append_numbers(numbers)
    except OnlyNumbersException as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f'\n{numbers}')
        break
