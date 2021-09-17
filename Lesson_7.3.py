class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        summ = self.parts + other.parts
        return print(f"В Новой клетке стало: {summ} яч.")

    def __sub__(self, other):
        sub = self.parts - other.parts
        if sub >= 0:
            return print(f"В Новой клетке стало: {sub} яч.")
        else:
            print("Число яцеек во второй клетке больше чем в первой. Вычитание невозможно.")

    def __mul__(self, other):
        mul = self.parts * other.parts
        return print(f"В Новой клетке стало: {mul} яч.")

    def __truediv__(self, other):
        div = self.parts / other.parts
        return print(f"В Новой клетке стало: {int(div + 0.5)} яч.")

    def make_order(self, all):
        a = ''
        if self.parts <= all:
            a += '*' * self.parts
        else:
            for i in range(self.parts // all):
                a += "*" * all + '\n'
            a += "*" * (self.parts % all)
        return a


cell_1 = Cell(15)
print(cell_1.make_order(6))
cell_2 = Cell(5)
cell_1 - cell_2
cell_1 + cell_2
cell_1 * cell_2
cell_1 / cell_2


















