dados = {'nome' : ['Amanda','clara'], 'idade' : ['17','16']}
dados['sexo'] = ['F', 'F'] #Adiciona um valor
del dados['idade'] #Remove um valor
info = []
info = dados.append()

print(dados.values()) #Retorna a ['Amanda','clara'], ['17','16'] e ['F', 'F']
print(dados.keys()) #Retorna ao nome, idade e sexo
for x,y in dados.items(): # o items pega de forma mais clara os items do dicionário
    print((x),(y))

print(*dados) # Retorna as keys
print(info)