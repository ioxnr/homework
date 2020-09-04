def int_func(*args):
    text = ' '.join(args)

    return text.title()


print(int_func(input('Введите несколько слов через пробел: ')))
