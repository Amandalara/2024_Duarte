class circulo():
    def __init__(self,raio,pi):
        self.raio = raio
        self.pi = pi
    
    def medir_circuferencia(self):
        return 2*self.pi * self.raio
    def medir_area(self):
        return 2*self.pi * self.raio**2

print(circulo(2,3.14).medir_circuferencia())


