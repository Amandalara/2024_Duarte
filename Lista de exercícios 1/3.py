class conta_bancaria:
    def __init__(self):
        self.nome = ''
        self.saldo = 0
        self.sacar = 0 
        self.depositar = 0
    
    def saque(self):
        print('Dinheiro disponível para o saque:', self.saldo)
        if self.saldo >= self.sacar:
            return self.sacar - self.saldo
        else:
            print('dinheiro indisponível para o saque!')
    
    def depósito(self):
        return self.saldo + self.depositar
    
x = conta_bancaria()
x.nome = 'Amanda Lara'
x.saldo = 1000
x.sacar = 500
x.saldo = 0

print(x.saque())



 
