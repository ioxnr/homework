class Road:
    length: int
    width: int

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self, asphalt_mass, thickness):
        return self._length * self._width * asphalt_mass * thickness


mass = Road(20, 5000)
print(mass.weight(25, 5))
