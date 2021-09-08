class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        gfn = self.name + " " + self.surname
        return gfn

    def get_total_income(self):
        gti = self._income["wage"] + self._income["bonus"]
        return gti


q = Position("Grigoriy", "Gerasimov", "chemestry", 400, 500)
print(q.name)
print(q.surname)
print(q._income)
print(q.get_full_name())
print(q.get_total_income())