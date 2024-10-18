import math

class Bhaskara:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = self.Delta()  # Calculate delta on initialization

    def __str__(self):
        return f'a = {self.__a}, b = {self.__b}, c = {self.__c}, delta = {self.__delta}'

    def Delta(self):
        self.__delta = self.__b**2 - 4 * self.__a * self.__c
        return self.__delta

    def TemRaizesReais(self):
        return self.__delta >= 0

    def raiz1(self):
        if self.TemRaizesReais():
            return (-self.__b + math.sqrt(self.__delta)) / (2 * self.__a)
        return True

    def raiz2(self):
        if self.TemRaizesReais():
            return (-self.__b - math.sqrt(self.__delta)) / (2 * self.__a)
        return False
