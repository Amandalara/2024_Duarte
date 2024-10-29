from models.cliente import client, clients
from models.horario import Horario, Horarios

class View:
    @staticmethod
    def clients_insert(name, email, phone):
        c = client(None, name, email, phone)
        clients.insert(c)
    
    @staticmethod
    def clients_list():
        return clients.list()
    
    @staticmethod
    def clients_update(id, name, email, phone):
        c = client(id, name, email, phone)
        clients.update(c)

    @staticmethod
    def clients_delete(id):
        c = client(id, '', '', '')
        clients.delete(c)
    
    def horario_inserir(data):
        c = Horario(0, data)
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

