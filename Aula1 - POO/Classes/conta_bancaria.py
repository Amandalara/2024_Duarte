class conta_bancaria():
    def __init__(self,titular,numero,saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def depósito(self):
        print(self.saldo)
        n = int(input('quanto deseja depósitar?'))
        return self.saldo - n
print(conta_bancaria('Amanda',986299589,2000))
        