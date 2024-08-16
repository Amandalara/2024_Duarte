from datetime import datetime


class paciente:
    def __init__(self, cpf,telefone,nome,nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nasc = nasc

        if nome == "":
            raise ValueError('Informe um nome válido!')
        
        if cpf == "":
            raise ValueError('Informe um cpf válido! ')
        
        if telefone == "":
            raise ValueError('Informe um telefone válido! ')
        
        if nasc > datetime.now():
            raise ValueError("Data de nascimento inválida")
    
    def idade(self):
        hoje = datetime.now()

        tempo = hoje - self.__nasc
        dias = tempo.days
        anos = dias // 360
        meses = dias % 365 // 30
    
    def __str__(self):
       return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nasc.strftime('%d/%m/%Y')}"
    
    class UI:
        @staticmethod

        def menu():
            print('1 - Cadastrar paciente 2 - mostrar paciente 3 - sair')
            return  int(input('Digite a opção:'))

        @staticmethod
        def main():
            respo = 0
            while respo != 3:
                respo = UI.menu()
                if respo == 1:
                    UI.new_patient()
        

        def new_patient():


