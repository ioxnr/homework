class OnlyNumbers(Exception):
    def __init__(self, *args):
        self.numbers = []

    def my_input(self):
        while True:
            try:
                values = input('Введите число: ')
                self.numbers.append(int(values))
                print(self.numbers)
            except:
                print('Недопустимое значение, введите число')


numb = OnlyNumbers(1)
print(numb.my_input())
