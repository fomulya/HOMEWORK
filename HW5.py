class Stationary:

    def __init__(self, title="Наименование"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
penc = Pencil()
pen = Pen()

mark.draw()
penc.draw()
pen.draw()