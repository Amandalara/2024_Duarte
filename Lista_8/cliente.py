import json
import streamlit as st


class Cliente:
    def __init__(self, id, nome, email, fone):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_fone(self):
        return self._fone

    def __str__(self):
        return f"{self._id} - {self._nome} - {self._email} - {self._fone}"


class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            m = max(c.get_id() for c in cls.objetos)
        else:
            m = 0
        obj._id = m + 1  
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c:
            c._nome = obj.get_nome()
            c._email = obj.get_email()
            c._fone = obj.get_fone()
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c:
            cls.objetos.remove(c)
            cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([{
                'id': c.get_id(),
                'nome': c.get_nome(),
                'email': c.get_email(),
                'fone': c.get_fone()
            } for c in cls.objetos], arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass