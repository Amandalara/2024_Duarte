import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_confirmado(self):
        return self.__confirmado

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_id_servico(self):
        return self.__id_servico

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def __str__(self):
        return f"{self.__id} - {self.__data}"

    def to_json(self):
        dic = {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico
        }
        return dic


class Horarios:
    __objetos = []  # atributo estático privado

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.__objetos:
            if c.id > m:
                m = c.id
        obj.id = m + 1
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.__objetos:
            if c.id == id:
                return c
        return None

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c is not None:
            c.data = obj.data
            c.confirmado = obj.confirmado
            c.id_cliente = obj.id_cliente
            c.id_servico = obj.id_servico
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c is not None:
            cls.__objetos.remove(c)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:  # w - write
            json.dump(cls.__objetos, arquivo, default=Horario.to_json)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:  # r - read
                texto = json.load(arquivo)
                for obj in texto:
                    c = Horario(
                        obj["id"],
                        datetime.strptime(obj["data"], "%d/%m/%Y %H:%M")
                    )
                    c.confirmado = obj["confirmado"]
                    c.id_cliente = obj["id_cliente"]
                    c.id_servico = obj["id_servico"]
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass
