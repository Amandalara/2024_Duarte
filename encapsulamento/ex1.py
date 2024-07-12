class triangulo():
  def __init__(self):
    self.b = 0
    self.h = 0

  def calcular_area(self):
    return self.b*self.h / 2

class UI:
  @staticmethod
  def main():
    opcao = 0
    while opcao != 2:
      opcao = UI.menu()
      if opcao == 1:
        UI.area_triangulo()
  @staticmethod

  def menu():
    print('1 - Calcular área')
    print('2 - Sair')
    opcao = int(input('Informe a opção desejada: '))
    return opcao  
  @staticmethod

  def area_triangulo():
    x = triangulo()
    x.b = float(input('Informe a base do triangulo: '))
    x.h = float(input('Informe a altura do triangulo: '))
    print('A área do triangulo é: ', x.calcular_area())

UI.main()