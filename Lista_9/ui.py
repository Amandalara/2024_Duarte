from views import View
from datetime import datetime

class UI:
    @staticmethod
    def menu():
        print("Costumer registration")
        print("1 - Insert 2 - List 3 - Update 4 - Delete")
        print("5 - Sair")
        return int(input("Enter the option:"))


    @staticmethod 
    def main():
        respo = 0
        while respo != 5:
            respo = UI.menu()
            if respo == 1: UI.insert_clients()
            if respo == 2: UI.list_clients()
            if respo == 3: UI.update_clients()
            if respo == 4: UI.delete_clients()

    @staticmethod
    def insert_clients():
        name = input("Enter your name:")
        email = input("Enter your name:")
        phone = input("Enter your name:")
        View.clients_insert(name, email, phone)
        

    @staticmethod
    def list_clients():
        for c in View.clients_list():
            print(c)

    @staticmethod
    def update_clients():
        UI.list_clients()
        id = int(input("Enter with person id:"))
        name = input("Enter your new name:")
        email = input("Enter your new email:")
        phone = input("Enter your new phone:")
        View.clients_update(id, name, email, phone)
        

    @staticmethod
    def delete_clients():
        UI.list_clients()
        id = int(input("Enter with person id:"))
        View.clients_delete(id)

    def horario_inserir():
    datastr = input("Informe uma data e horário no formato dd/mm/aaaa hh:mm: ")
    data = datetime.strptime(datastr, "%d/%m/%Y %H:%M")
    View.horario_inserir(data)


    @staticmethod
    def horario_listar():  
        for c in View.horario_listar():
            print(c)


    @staticmethod
    def horario_atualizar():
        pass


    @staticmethod
    def horario_excluir():
        pass
