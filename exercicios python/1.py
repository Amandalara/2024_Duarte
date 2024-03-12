print('digite uma data no formato dd/mm/aa')
data = input()
dia, mes, ano = data.split('/')
d = int(dia)
m = int(mes)
a = int(ano)
maior = 31
if m == 4 or m == 6 or m == 9 or m == 11:
    maior = 0 
if m == 2:
        if ano % 4 == 0 and ano % 100 != 0 and a % 400 == 0:
            maior = 29
        else:
            maior = 28

if a >=1900 and a<= 2100 and m>=1 and m<=12 and d>=1 and d<=maior:
   print('A data é válida')

else:
    print('A data é inválida')