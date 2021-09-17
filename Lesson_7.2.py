from abc import ABC, abstractmethod

class AllClothers(ABC):

    @abstractmethod
    def clothers(self):
        pass

class TopCoat(AllClothers):
    def __init__(self, v):
        self.v = v

    @property
    def clothers(self):
        return self.v / 6.5 + 0.5

class Suit(AllClothers):
    def __init__(self, h):
        self.h = h

    @property
    def clothers(self):
        return 2 * self.h + 0.3


topcoat = TopCoat(15)
suit = Suit(15)
print(topcoat.clothers)
print(suit.clothers)











# from abc import ABC, abstractmethod
#
# class MyAbstractClass(ABC):
#     @abstractmethod
#     def my_method_1(self, n1, n2):
#         pass
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
# class MyClass(MyAbstractClass):
#     def my_method_1(self, n1, n2):
#         print(f"Метод my_method_1({n1 + n2})")
#
#     def my_method_2(self):
#
#         print("Метод my_method_2()")
#
#
# mc = MyClass()
# mc.my_method_1(15, 25)



























