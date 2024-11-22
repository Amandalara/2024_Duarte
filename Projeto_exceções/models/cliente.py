import json

# Modelo Cliente
class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if not email.strip():
            raise ValueError("O e-mail não pode ser vazio.")
        self.__email = email

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        if not fone.strip():
            raise ValueError("O telefone não pode ser vazio.")
        self.__fone = fone

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        if not senha.strip():
            raise ValueError("A senha não pode ser vazia.")
        self.__senha = senha

    def __str__(self):
        return f"{self.__nome} - {self.__email} - {self.__fone}"

# Persistência
class Clientes:
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
            c.set_nome(obj.get_nome())
            c.set_email(obj.get_email())
            c.set_fone(obj.get_fone())
            c.set_senha(obj.get_senha())
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
        cls.__objetos.sort(key=lambda cliente: cliente.get_nome())
        return cls.__objetos

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:  # w - write
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:  # r - read
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(
                        obj['__id'],
                        obj['__nome'],
                        obj['__email'],
                        obj['__fone'],
                        obj['__senha']
                    )
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass
