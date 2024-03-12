f = input('digite uma frase:')

for x in range (len(f)):
    f = f[1:] + f[0]
    print(f)