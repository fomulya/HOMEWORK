class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_mass(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"

my_road = Road(5000, 20)
print(my_road.road_mass())