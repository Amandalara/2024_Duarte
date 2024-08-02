class time():
    def __init__(self):
        self.__nome = ''
        self.__estado = ''
        self.__jogadores = []
    
    def set_nome(self,name):
        if self.__nome != '':
            self.__nome = name
        else:
            raise ValueError('Dado inválido!!')
    def get_nome(self):
        return self.__nome
    
    def set_estado(self,name):
        if self.__estado != '':
            self.__estado = name
        else:
            raise ValueError('Dado inválido!!')
    def get_estado(self):
        return self.__estado
        
    def inserir(self,jo):
        self.__jogadores.append(jo)
    
    def listar(self):
        return self.__jogadores[:]
    

class Jogadores():
    jogador_nome = input('Digite o nome do jogador:')
    camisa = int(input('Digite o número da camisa:'))

    def __str__(self,jogador_nome,camisa):
        return f'O nome do jogador é: {jogador_nome} e o número da sua camisa é: {camisa}'

class UI():

    def main():
        respo = 0
        while respo != 2:
            respo = UI.menu()
            if respo == 1:
                UI.inserir()

    def menu():
        print('Digite 1 para criar um nome time:')
        print('Digite 2 para sair:')
        return int(input('Digite 1 ou 2:'))

    def inserir_jogadores(jo):
        x = Jogadores()
        
    



  