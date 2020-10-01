class Division:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    def divide(self):
        if self.dividend == 0:
            raise ZeroDivisionErrorException
        else:
            return self.divider / self.dividend


class ZeroDivisionErrorException(Exception):

    def __str__(self):
        return 'Делить на ноль недопустимо'


div = Division(10, 0)
try:
    print(div.divide())
except ZeroDivisionErrorException as exception:
    print('Делить на ноль нельзя')
