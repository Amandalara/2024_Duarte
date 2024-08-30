import json
from datetime import datetime

class horario:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.confirmado = False
        self.id_cliente = 0
        self.id_servico = 0
    
    def __str__(self):
        return f'{self.id} - {self.data}'
    
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["data"] = self.data.strftime("%d/%m/%Y %H:%M") 
        dic["confirmado"] = self.confirmado
        dic["id_cliente"] = self.id_cliente
        dic["id_servico"] = self.id_servico
        return dic

class horarios:
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
        return None # porque esse return none?
        
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def atualizar(cls,obj):
        c = cls.listar_id(obj.id)
        if c != None: #nao entendi esse if com o None
            c.data = obj.data
            c.confirmado = obj.confirmado
            c.id_cliente = obj.id_cliente
            c.id_servico = obj.id_servico
            cls.salvar()
    
    @classmethod
    def excluir(cls,obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.objetos.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default= horario.to_json)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horarios.json", mode='r') as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = horario(obj["id"],datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
                    c.confirmado = obj["confirmado"]
                    c.id_cliente = obj["id_cliente"]
                    c.id_servico = obj["id_servico"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass