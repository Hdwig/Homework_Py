from time import sleep

class TrafficLight:
    color = ("red", "yellow", "green")
    time = (7, 2, 4)
    def __init__(self):
        self.__colore = "yellow"

    def running(self):
        while True:
            for i in self.color:
                self.__colore = i
                print(self.__colore)
                sleep(self.time[self.color.index(self.__colore)])

t = TrafficLight()
t.running()





