

class Auto:
    """

    This is auto
    """
    count = 10

    def __init__(self, model):
        self.model = model

    @staticmethod
    def buy_car(price, count):
        print(f"Поздравляю! вы купиль {count} za {price}")

    @classmethod
    def get_count(cls):
        print(f"You got {cls.count} auto!")

    def get_car_model(self):
        print(self.model)


Auto.buy_car(1000000, 3)
Auto.get_count()
car = Auto("Tesla model X")
car.get_car_model()
print(Auto.__name__)
print(car.__dict__)
print(car.__doc__)
print(car.__str__)
print(car.__module__)
# 1.27.00


Name = 0

