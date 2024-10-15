import math

class Bhaskara:
    def __init__(self,a,b,c,delta):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = delta
    def __str__(self):
        return f'a = {self.__a}, b = {self.__b}, c = {self.__c}, self.__delta = {self.__delta}'
    def Delta(self):
        self.__delta = self.__b**2 - 4 * self.__a * self.__c
        return self.__delta
    def TemRaizesReais(self):
        if self.__delta >= 0:
            return True
        else:
            return False
    def raiz1(self):
        return -self.__b + math. sqrt(self.delta) / 2* self.__a
    def raiz2(self):
        return self.__b + math. sqrt(self.delta) / 2* self.__a
    


        
        