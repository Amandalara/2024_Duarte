import json

class cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.fone = fone
        self.nome = nome
        self.email = email
    
    def __str__(self):
        return f'{self.id} - {self.nome} - {self.email} - {self.fone}'

class clientes: 
    objetos = []
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m:
                c.id = m
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for c in cls.objetos:
            if c.id == id:
                return c
        return None 
        
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def atualizar(cls,obj):
        c = cls.listar_id(obj.id)
        if c != None: #se o id existir, ou seja, diferente de None, o cliente será atualizado
            c.nome = obj.nome
            c.email = obj.email
            c.fone = obj.fone
            cls.salvar()
    
    @classmethod
    def excluir(cls,obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.objetos.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default= vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode='r') as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = cliente(obj["id"],obj["nome"], obj["email"], obj["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

