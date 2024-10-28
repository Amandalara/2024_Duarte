from models.cliente import client,clients


class view:
    def clients_insert(name, email, phone):
        c = client(0, name, email, phone)
        clients.insert(c)
    
    def clients_list():
        return clients.list()
    
    def clients_update(id, name, email, phone):
        c = client(id, name, email, phone)
        clients.update(c)

    def clients_delete():
        c = client(id , '', '', '')
        clients.delete(c)