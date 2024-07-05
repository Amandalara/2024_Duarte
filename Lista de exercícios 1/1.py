class circulo():
    def __init__(self):
        self.raio = 0
        self.pi = 3.14

    def calcular_area(self):
        return self.pi * self.raio ** 2
    
    def calcular_circuferencia(self):
        return 2 * self.pi * self.raio
    
x1 = circulo()
x1.raio = 2
print(x1.calcular_area()) 
print(x1.calcular_circuferencia()) 