import json 

class Perfil: 
    def __init__(self, nome, descricao, beneficios):
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.beneficios}'


class Perfis:
    