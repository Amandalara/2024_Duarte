contador = 10
nome = input('NOME:')
matricula = input('MATRICULA:')
ano = ''
lista = []

while contador != 0:
    for s in range(0,4):
        ano += matricula[s]
        contador = contador - 1
        print(f'nome:{nome}, matricula:{matricula}')
        nome = input('NOME:')
        matricula = input('MATRICULA:')

    

