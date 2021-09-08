class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Ваша скорость равна: {self.speed}")

    def go(self):
        print("машина едет")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print(f"машина поехала в {direction} направлении ")


class TownCar(Car):
    def show_speed(self):
        speed = float(self.speed)
        if speed > 60:
            print(f"Ваша скорость {speed}, это выше ограничения в 60 км\ч")
        else:
            print(f"Ваша скорость равна: {speed}")
        return self.show_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        speed = float(self.speed)
        if speed > 40:
            print(f"Ваша скорость {speed}, это выше ограничения в 60 км\ч")
        else:
            print(f"Ваша скорость равна: {speed}")
        return self.show_speed


class PoliceCar(Car):
    pass


towncar = TownCar(20, "yellow", "t", False)
sportcar = SportCar(130, "pink", "s", False)
workcar = WorkCar(95, "orange", "w", False)
polisecar = PoliceCar(15, "black", "p", True)

towncar.show_speed()
sportcar.show_speed()
sportcar.go()
sportcar.turn("левом")
polisecar.go()
workcar.stop()
workcar.go()
workcar.show_speed()
