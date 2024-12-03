import json 

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha): 
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'{self.nome} - {self.especialidade} - {self.conselho} - {self.email}'