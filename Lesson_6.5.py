class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Записываем что-то ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Пишем карандашем.")


class Handle(Stationery):
    def draw(self):
        print("Выделяем маркером")


pen = Pen("")
pencil = Pencil("")
handle = Handle("")
pen.draw()
pencil.draw()
handle.draw()