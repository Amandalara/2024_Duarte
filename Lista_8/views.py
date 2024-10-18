from cliente import Cliente, Clientes

def cliente_inserir(nome, email, fone):
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

def cliente_listar():
    return Clientes.listar()    
  
def cliente_atualizar(id, nome, email, fone):
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

def cliente_excluir(id):
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)    