from views import view

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
        

    @staticmethod
    def list_clients():

    @staticmethod
    def update_clients():

    @staticmethod
    def delete_clients():
