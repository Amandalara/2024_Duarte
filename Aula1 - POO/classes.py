class aluno:
    def __init__(self):
        self.nome = ''
        self.matricula = ''

a  = aluno()
a.nome= 'igor'
a.matricula = '20241011110014'
b  = aluno()
b.nome = 'clara'
b.matricula = '20211011110009'
print(a)
print(a.nome, a.matricula,a.ano())
print(b)
print(b.nome, b.matricula,b.ano())
 
