import json

# Modelo
class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
        self.set_duracao(duracao)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if not descricao or not descricao.strip():  # Verifica se a descrição é vazia ou só tem espaços
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        if valor < 0:  # Verifica se o valor é negativo
            raise ValueError("O valor não pode ser negativo.")
        self.__valor = valor

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        if duracao < 0:  
            raise ValueError("A duração não pode ser negativa.")
        self.__duracao = duracao

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"


# Persistência
class Servicos:
    __objetos = []  # atributo estático 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.__objetos:
            if c.get_id() > m:
                m = c.get_id()
        obj.set_id(m + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_descricao(obj.get_descricao())
            c.set_valor(obj.get_valor())
            c.set_duracao(obj.get_duracao())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c is not None:
            cls.__objetos.remove(c)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:  # w - write
            json.dump(cls.__objetos, arquivo, default=lambda o: o.__dict__)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:  # r - read
                texto = json.load(arquivo)
                for obj in texto:
                    c = Servico(
                        obj["_Servico__id"],
                        obj["_Servico__descricao"],
                        obj["_Servico__valor"],
                        obj["_Servico__duracao"]
                    )
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass
