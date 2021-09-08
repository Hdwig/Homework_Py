class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def running(self):
        mas = 25
        tol = 5
        print(f"Для покрытия дороги толщиной 5 см надо: {self._lenght * self._width * mas * tol} тонн")


a = Road(15, 25)
a.running()



