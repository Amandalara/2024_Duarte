class viagem:
  def __init__(self):
    self.distancia = 0
    self.horas = 0
    self.minutos = 0

  def velocidade_media(self):
    return self.distancia / (self.horas + self.minutos / 60)
  
x1 = viagem()
x1.distancia = 2
x1.horas = 2
x1.minutos = 10

print('A velocidade é',x1.velocidade_media(),'km/h')
