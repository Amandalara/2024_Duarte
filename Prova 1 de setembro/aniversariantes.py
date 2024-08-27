
import json
from datetime import datetime
from datetime import date

class Paciente:
  def __init__(self, id, nome, nasc, fone):
    self.id = id
    self.nome = nome
    self.nasc = nasc
    self.fone = fone
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.nasc} - {self.fone}"


class Pacientes:
  objetos = []    # atributo estático
  @classmethod
  def inserir(pac, obj):
    pac.abrir()
    m = 0
    for c in pac.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    pac.objetos.append(obj)
    pac.salvar()
  @classmethod
  def listar_id(pac, id):
    pac.abrir()
    for c in pac.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(pac, obj):
    c = pac.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.nasc = obj.nasc
      c.fone = obj.fone
      pac.salvar()

  @classmethod
  def excluir(pac, obj):
    c = pac.listar_id(obj.id)
    if c != None:
      pac.objetos.remove(c)
      pac.salvar()
  
  @classmethod
  def listar(pac):
    pac.abrir()
    return pac.objetos
  @classmethod
  def salvar(pac):
    with open("pacientes.json", mode="w") as arquivo:   # w - write
      json.dump(pac.objetos, arquivo, default = vars)
  @classmethod
  def abrir(pac):
    pac.objetos = []
    with open("pacientes.json", mode="r") as arquivo:   # r - read
      texto = json.load(arquivo)
      for obj in texto:   
        c = Paciente(obj["id"], obj["nome"], obj["nasc"], obj["fone"])
        pac.objetos.append(c)
  @classmethod
  def aniversariantes(pac,obj):
    pac.abrir()
    pac.niver = []
    for obj in pac.niver:
      c = Paciente(obj["nasc"])
      pac.niver.append(c)
    for obj in pac.niver:
      if obj:
        print(obj)


class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - Listar pacientes, 3 - atualizar cliente, 4 - excluir cliente, 5 - ver aniversariantes 9 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9:
      op = UI.menu()
      if op == 1: UI.paciente_inserir()
      if op == 2: UI.paciente_listar()
      if op == 3: UI.paciente_atualizar()
      if op == 4: UI.paciente_excluir()
      if op == 5: UI.paciente_aniversariantes()

  @staticmethod
  def paciente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    nasc = input("Informe a data de nascimento: (dd/mm/aa):")
    fone = input("Informe o fone: ")
    c = Paciente(0, nome, nasc, fone)
    Pacientes.inserir(c)

  @staticmethod
  def paciente_listar():  
    for c in Pacientes.listar():
      print(c)

  @staticmethod
  def paciente_atualizar():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    nasc = input("Informe a nova data de nascimento: ")
    fone = input("Informe o novo fone: ")
    c = Paciente(id, nome, nasc, fone)
    Pacientes.atualizar(c)

  @staticmethod
  def paciente_excluir():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser excluído: "))
    c = Paciente(id, "", "", "")
    Pacientes.excluir(c)

  @staticmethod
  def paciente_aniversariantes():
    mes = int(input('Digite o mês que deseja ver os aniversariantes:'))
    c = mes
    c = Paciente("", "", nasc, "")
    Pacientes.aniversariantes(c)

    
      
UI.main()