class Matrix:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f"{self.first[0]} {self.second[0]} {self.third[0]} \n{self.first[1]} {self.second[1]} {self.third[1]}"

    def __add__(self, other):
        result_11 = self.first[0] + other.first[0]
        result_21 = self.second[0] + other.second[0]
        result_31 = self.third[0] + other.third[0]
        result_12 = self.first[1] + other.first[1]
        result_22 = self.second[1] + other.second[1]
        result_32 = self.third[1] + other.third[1]
        return f"{result_11} {result_21} {result_31} \n{result_12} {result_22} {result_32}"


o = Matrix((1, 2), (3, 4), (5, 6))
n = Matrix((1, 2), (3, 4), (5, 6))
print(o)
print(n)
print(o + n)














