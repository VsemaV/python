class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск зарисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Ручка рисует')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Маркер рисует')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()
