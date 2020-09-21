class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'The car is going'

    def stop(self):
        return 'The car has stopped'

    def turn(self, direction):
        return f'The car has turned {direction}'

    def show_speed(self):
        return f'Current speed is - {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed is - {self.speed}')
        if self.speed > 60:
            return 'Speed exceeded'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed is - {self.speed}')
        if self.speed > 40:
            return 'Speed exceeded'


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = Car(70, 'white', 'Audi', False)
bmw = TownCar(120, 'black', 'BMW', False)
ford = SportCar(130, 'yellow', 'Ford', False)
nissan = WorkCar(80, 'red', 'Nissan', False)
lada = PoliceCar(60, 'grey', 'Lada', True)

print(f'The color of {audi.name} - {audi.color}')
print(f'{ford.name} speed is {ford.speed}')
print(nissan.show_speed())
print(bmw.show_speed())
print(lada.go())
print(ford.stop())
print(bmw.turn('left'))
